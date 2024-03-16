from datetime import datetime

from src.app import app
from src.celery_config import celery_app
from src.dependency_container import DependencyContainer


@celery_app.task
def send_scheduled_emails():
    with app.app_context():
        container = DependencyContainer()
        email_repository = container.email_repository()
        email_service = container.email_service()

        emails_to_send = email_repository.find({"need_send_email": True})

        for email in emails_to_send:
            email_service.send_email(email.id)
