from src.infrastructure.models import Email
from src.infrastructure.repositories.repository import Repository


class EmailRepository(Repository):
    base_class = Email
    DEFAULT_NOT_FOUND_MESSAGE = "Email was not found"
