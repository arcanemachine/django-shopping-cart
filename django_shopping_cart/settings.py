"""Generated by 'django-admin startproject' using Django 3.1.5."""

from pathlib import Path

from django_shopping_cart import secret_key, server_config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = server_config.BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = server_config.DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

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
        'DIRS': server_config.TEMPLATE_DIRS,
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


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': server_config.DB_NAME,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = server_config.STATICFILES_DIRS
STATIC_ROOT = server_config.STATIC_ROOT


# authentication

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'users:user_detail'
LOGOUT_REDIRECT_URL = 'project_root'

# corsheaders

CORS_ALLOWED_ORIGINS = server_config.CORS_ALLOWED_ORIGINS
CORS_ALLOW_ALL_ORIGINS = server_config.CORS_ALLOW_ALL_ORIGINS

# media files

MEDIA_ROOT = server_config.MEDIA_ROOT
MEDIA_URL = '/media/'


# rest_framework

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny'],
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication']
    }
