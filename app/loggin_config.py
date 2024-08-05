import json
import logging
import sys
import uuid
from time import time

from flask import request, g


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        record.method = request.method
        record.headers = json.dumps(dict(request.headers))
        record.payload = json.dumps(
            request.get_json(silent=True) or request.form.to_dict() or None
        )
        if hasattr(g, "response"):
            record.response = json.dumps(g.response)
        if hasattr(g, "request_time"):
            record.request_time = g.request_time
        return super().format(record)


def setup_logging(app):
    formatter = RequestFormatter(
        "%(asctime)s [%(levelname)s] %(remote_addr)s requested %(url)s\n"
        "Headers: %(headers)s\n"
        "Payload: %(payload)s\n"
        "Response: %(response)s\n"
        "Time taken: %(request_time).2f ms\n"
    )

    # Create console handler and set level to debug
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Remove existing handlers and add console handler
    app.logger.handlers.clear()
    app.logger.addHandler(console_handler)
    app.logger.setLevel(app.config["LOG_LEVEL"])

    # Log request info before processing
    @app.before_request
    def log_request_info():
        g.start_time = time()
        g.trace_id = uuid.uuid4()

    @app.after_request
    def log_response_info(response):
        if not hasattr(g, "start_time"):
            g.start_time = time()

        g.request_time = (time() - g.start_time) * 1000
        g.response = {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "data": response.get_data(as_text=True),
        }

        app.logger.info(f"Request completed")

        return response
