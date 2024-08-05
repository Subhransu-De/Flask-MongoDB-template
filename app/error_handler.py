from flask import jsonify


def setup_error_handler(app):
    @app.errorhandler(Exception)
    def handle_exception(e):
        # Default HTTP status code
        code = 500
        if hasattr(e, "code"):
            code = e.code

        # Log the error
        # logger.error(f"Error: {e}", exc_info=True)

        # Response
        response = {
            "message": str(e),
            "error": "Internal Server Error" if code == 500 else "Error",
        }
        return jsonify(response), code
