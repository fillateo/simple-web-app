from datetime import datetime

from src.infrastructure.models import Email
from src.infrastructure.repositories.repository import Repository


class EmailRepository(Repository):
    base_class = Email
    DEFAULT_NOT_FOUND_MESSAGE = "Email was not found"

    def _apply_query_params(self, query, query_params):
        need_send_email = self.get_query_param("need_send_email", query_params)
        if need_send_email:
            current_time = datetime.now()

            query = query.filter(self.base_class.timestamp <= current_time).filter_by(
                sent=False
            )

        return query
