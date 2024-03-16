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

        current_time = datetime.now()
        emails_to_send = email_repository.find(
            {
                "sent": False,
                "timestamp": email_repository.base_class.timestamp <= current_time,
            }
        )

        for email in emails_to_send:
            email_service.send_email(email.id)
