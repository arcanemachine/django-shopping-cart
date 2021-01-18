from os.path import join as os_path_join
from pathlib import Path

SERVER_NAME = 'dev'
SERVER_LOCATION = '192.168.1.120:8000'
DEBUG = True

BASE_DIR = str(Path(__file__).resolve().parent)

DB_NAME = os_path_join(BASE_DIR, 'db.sqlite3')

MEDIA_ROOT = os_path_join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os_path_join(BASE_DIR, 'static')]
TEST_SPEC_DIRS = [os_path_join(BASE_DIR, 'jasmine/jasmine/')]
STATIC_ROOT = None
