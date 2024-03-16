import logging

from dependency_injector.wiring import Provide, inject
from flask import Blueprint

from src.api.middleware import post_data_required
from src.api.responses import create_response
from src.api.schemas import EmailSchema
from src.dependency_container import DependencyContainer

logger = logging.getLogger(__name__)
blueprint = Blueprint("email", __name__)


@blueprint.route("/email", methods=["POST"])
@post_data_required
@inject
def save_email(json_data, email_service=Provide[DependencyContainer.email_service]):
    validated_data = EmailSchema().load(json_data)
    service_email = email_service.create(data=validated_data)
    return create_response(service_email, EmailSchema)
