from os.path import join as os_path_join
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent)
DEBUG = True
ALLOWED_HOSTS =\
    ['*']

PROJECT_NAME = "Django Shopping Cart"
SERVER_NAME = 'dev'
SERVER_LOCATION = 'http://localhost:8004'

FRONTEND_SERVER_LOCATION = 'http://localhost:8080'

CORS_ALLOWED_ORIGINS = \
    []
CORS_ALLOW_ALL_ORIGINS = True
