import logging
from typing import Tuple

from flask import jsonify, Response

from app.exception.not_found_exception import NotFoundException


# TODO: Log the error.
# TODO: More descriptive error.
def setup_error_handler(app) -> None:
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
