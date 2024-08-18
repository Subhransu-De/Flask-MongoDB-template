import logging
from typing import Tuple

from flask import jsonify, Response
from pydantic import ValidationError

from app.exception.not_found_exception import NotFoundException


def setup_error_handler(app) -> None:
    @app.errorhandler(ValidationError)
    def handle_bad_request(error: ValidationError):
        return (
            jsonify(
                {
                    "message": [
                        f'{err.get("loc")[0]} : {err.get("msg")}'
                        for err in error.errors()
                    ]
                }
            ),
            400,
        )

    @app.errorhandler(NotFoundException)
    def handle_not_found(e: NotFoundException) -> Tuple[Response, int]:
        return (
            jsonify({"error": e.message if e.message else "Resource not found."}),
            404,
        )

    @app.errorhandler(Exception)
    def handle_exception(e: Exception) -> Tuple[Response, int]:
        logging.error(e)
        return jsonify({"error": "An internal server error has occurred."}), 500
