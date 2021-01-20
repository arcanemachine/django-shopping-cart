from os.path import join as os_path_join
from pathlib import Path

PROJECT_NAME = "Django Shopping Cart"
SERVER_NAME = 'dev'
SERVER_LOCATION = 'http://192.168.1.100:8000'
DEBUG = True

FRONTEND_SERVER_LOCATION = 'http://192.168.1.100:8080'
FRONTEND_LOGIN_URL = '/login/'

BASE_DIR = str(Path(__file__).resolve().parent.parent)

CORS_ALLOWED_ORIGINS = ['http://localhost:8080']
CORS_ALLOW_ALL_ORIGINS = False

DB_NAME = os_path_join(BASE_DIR, 'db.sqlite3')

MEDIA_ROOT = os_path_join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os_path_join(BASE_DIR, 'static')]
STATIC_ROOT = None

TEMPLATE_DIRS = [os_path_join(BASE_DIR, 'templates')]
