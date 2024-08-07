from typing import Tuple

from bson import ObjectId
from flask import Blueprint, request, jsonify, Response

from ..models.input.user_input import UserInput
from ..services.user_service import UserService

user_blueprint = Blueprint("user", __name__, url_prefix="users")
user_service = UserService()


@user_blueprint.route("/", methods=["POST"])
def create() -> Tuple[Response, int]:
    user = UserInput(**request.json)
    return jsonify(user_service.create_user(user).model_dump()), 201


@user_blueprint.get("/<user_id>")
def get(user_id):
    user = user_service.get_user(user_id)
def get(user_id) -> Tuple[Response, int]:
    if user:
        return jsonify(user.model_dump()), 200
    return jsonify({"message": f"User with id '{user_id}' not found."}), 404


@user_blueprint.get("/")
def get_all():
    return jsonify([user.model_dump() for user in user_service.get_all_users()]), 200
def get_all() -> Tuple[Response, int]:


@user_blueprint.put("/<user_id>")
def update(user_id):
    user_data = request.json
    success = user_service.update_user(user_id, user_data)
    if success:
        return jsonify({"message": "User updated"}), 200
    return jsonify({"message": "User not found"}), 404
def update(user_id) -> Tuple[Response, int]:


@user_blueprint.delete("/<user_id>")
def delete(user_id) -> Tuple[Response, int]:
    user_service.delete(user_id)
    return jsonify(), 204


@user_blueprint.get("/paginated")
def get_paginated() -> Tuple[Response, int]:
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    result = user_service.get_users_paginated(page, per_page)
    return jsonify(result), 200
