import logging

from src.domain.exceptions import ApiException
from src.services.repository_service import RepositoryService

logger = logging.getLogger(__name__)


class EmailService(RepositoryService):
    def __init__(self, repository, event_repository):
        super().__init__(repository)
        self.event_repository = event_repository

    def create(self, data):
        event_id = data.get("event_id")
        event = self.event_repository.get(event_id)

        if not event:
            raise ApiException(message=f"Event with id {event_id} not found")

        return super().create(data)

    def send_email(self, email_id):
        email = self.repository.update(email_id, {"sent": True})
        event = self.event_repository.get(email.event_id)

        for user in event.users:
            logger.info(f"Send email with id {email_id} to {user.email}")
