from functools import wraps

from flask import request

from src.domain import NoDataProvidedApiException


def post_data_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        json_data = request.get_json()
        if json_data is None or json_data == {}:
            raise NoDataProvidedApiException()
        else:
            return f(json_data, *args, **kwargs)

    return wrapped
