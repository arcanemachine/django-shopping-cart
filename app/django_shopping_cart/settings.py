import os

from django_shopping_cart import server_config

SECRET_KEY = os.environ['SECRET_KEY']

BASE_DIR = server_config.BASE_DIR
DEBUG = server_config.DEBUG
ALLOWED_HOSTS = server_config.ALLOWED_HOSTS


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local
    'stores.apps.StoresConfig',
    'users.apps.UsersConfig',
    # third-party
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_shopping_cart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(server_config.BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_shopping_cart.context_processors.constants',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_shopping_cart.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(server_config.BASE_DIR, 'db.sqlite3'),
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# password validation
pv_prefix = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{pv_prefix}.UserAttributeSimilarityValidator'},
    {'NAME': f'{pv_prefix}.MinimumLengthValidator'},
    {'NAME': f'{pv_prefix}.CommonPasswordValidator'},
    {'NAME': f'{pv_prefix}.NumericPasswordValidator'}]

# internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# authentication
LOGIN_URL = 'project_root'
LOGIN_REDIRECT_URL = 'project_root'
LOGOUT_REDIRECT_URL = 'project_root'

# static
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/staticfiles/'


# media files
MEDIA_ROOT = os.path.join(server_config.BASE_DIR, 'media')
MEDIA_URL = '/media/'

# corsheaders
CORS_ALLOWED_ORIGINS = server_config.CORS_ALLOWED_ORIGINS
CORS_ALLOW_ALL_ORIGINS = server_config.CORS_ALLOW_ALL_ORIGINS

# rest_framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny'],
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication']
    }
