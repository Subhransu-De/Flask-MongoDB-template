from typing import Tuple

from flask import Blueprint, Response
from injector import inject

from app.services.user_service import UserService

user_blueprint = Blueprint("user", __name__, url_prefix="users")


@inject
@user_blueprint.post("")
def create(user_service: UserService) -> Tuple[Response, int]:
    pass


@inject
@user_blueprint.get("")
def get_all(user_service: UserService) -> Tuple[Response, int]:
    pass


@inject
@user_blueprint.get("/paginated")
def get_paginated(user_service: UserService, user_id: str) -> Tuple[Response, int]:
    pass


@inject
@user_blueprint.get("/<user_id>")
def get(user_service: UserService, user_id: str) -> Tuple[Response, int]:
    pass


@inject
@user_blueprint.put("/<user_id>")
def update(user_service: UserService, user_id: str) -> Tuple[Response, int]:
    pass


@inject
@user_blueprint.delete("/<user_id>")
def delete(user_service: UserService, user_id: str) -> Tuple[Response, int]:
    pass
