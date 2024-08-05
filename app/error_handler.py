from typing import Tuple

from flask import jsonify, Response


def setup_error_handler(app) -> None:
    @app.errorhandler(Exception)
    def handle_exception(e) -> Tuple[Response, int]:
        code = 500
        if hasattr(e, "code"):
            code = e.code

        # TODO: Log the error.
        # TODO: Logging of different types of error is configurable.

        response = {
            "message": str(e),
            "error": "Internal Server Error" if code == 500 else "Error",
        }
        return jsonify(response), code
