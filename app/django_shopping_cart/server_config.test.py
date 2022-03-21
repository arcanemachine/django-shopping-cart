from os.path import join as os_path_join
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent)
DEBUG = False
ALLOWED_HOSTS =\
    ['django-shopping-cart.test.moendigitalservices.com']

PROJECT_NAME = "Django Shopping Cart"
SERVER_NAME = 'prod'
SERVER_LOCATION =\
    'https://django-shopping-cart.test.moendigitalservices.com/'  # noqa: E501

FRONTEND_SERVER_LOCATION = 'https://vue-shopping-cart2.surge.sh/'

CORS_ALLOWED_ORIGINS = \
    ['https://django-shopping-cart.test.moendigitalservices.com']  # noqa: E501
CORS_ALLOW_ALL_ORIGINS = False