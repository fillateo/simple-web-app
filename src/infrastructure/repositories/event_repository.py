from src.infrastructure.models import Event
from src.infrastructure.repositories.repository import Repository


class EventRepository(Repository):
    base_class = Event
    DEFAULT_NOT_FOUND_MESSAGE = "Event was not found"
