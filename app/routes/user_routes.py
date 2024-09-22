from typing import Tuple

from flask import Blueprint, Response, request, jsonify
from injector import inject

from app.models.input import UserInput
from app.models.output import UserOutput
from app.services.user_service import UserService

user_blueprint = Blueprint("user", __name__, url_prefix="users")


@inject
@user_blueprint.post("")
def create(user_service: UserService) -> Tuple[Response, int]:
    user_input: UserInput = UserInput(**request.get_json())
    response: UserOutput = user_service.create(user_input)
    return jsonify(response.model_dump(by_alias=True)), 201


@inject
@user_blueprint.get("/<user_id>")
def get(user_service: UserService, user_id: str) -> Tuple[Response, int]:
    response = user_service.get(user_id)
    return jsonify(response.model_dump(by_alias=True)), 201


@inject
@user_blueprint.get("")
def get_all(user_service: UserService) -> Tuple[Response, int]:
    pass


@inject
@user_blueprint.put("/<user_id>")
def update(user_service: UserService, user_id: str) -> Tuple[Response, int]:
    pass


@inject
@user_blueprint.delete("/<user_id>")
def delete(user_service: UserService, user_id: str) -> Tuple[Response, int]:
    user_service.delete(user_id)
    return jsonify(), 204
