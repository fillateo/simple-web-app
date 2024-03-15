from src.infrastructure.models import Email
from src.infrastructure.repositories.repository import Repository


class EmailRepository(Repository):
    base_class = Email
    DEFAULT_NOT_FOUND_MESSAGE = "Email was not found"

    def _apply_query_params(self, query, query_params):
        name_query_param = self.get_query_param("name", query_params)

        if name_query_param:
            query = query.filter_by(name=name_query_param)
        return query
