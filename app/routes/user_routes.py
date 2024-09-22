from typing import Tuple, List

from flask import Blueprint, Response, request, jsonify
from injector import inject

from app.models.input import UserInput
from app.models.output import UserOutput, Paginated
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
    response: UserOutput = user_service.get(user_id)
    return jsonify(response.model_dump(by_alias=True)), 200


@inject
@user_blueprint.get("")
def get_all(user_service: UserService) -> Tuple[Response, int]:
    start: str = request.args.get("start")
    limit: str = request.args.get("limit")
    if start is not None and limit is not None:
        if int(start) > 0 and int(limit) >= 0:
            response: Paginated[UserOutput] = user_service.get_all_paginated(
                int(start), int(limit)
            )
            return jsonify(response.model_dump(by_alias=True)), 200
        else:
            raise ValueError("Bad pagination query.")
    else:
        response: List[UserOutput] = user_service.get_all()
        return jsonify([res.model_dump(by_alias=True) for res in response]), 200


@inject
@user_blueprint.put("/<user_id>")
def update(user_service: UserService, user_id: str) -> Tuple[Response, int]:
    user_input: UserInput = UserInput(**request.get_json())
    response: UserOutput = user_service.update(user_id, user_input)
    return jsonify(response.model_dump(by_alias=True)), 200


@inject
@user_blueprint.delete("/<user_id>")
def delete(user_service: UserService, user_id: str) -> Tuple[Response, int]:
    user_service.delete(user_id)
    return jsonify(), 204
