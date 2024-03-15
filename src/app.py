import logging

from src import api
from src.config import Config
from src.create_app import create_app

logger = logging.getLogger(__name__)
app = create_app(Config, dependency_container_packages=[api])
