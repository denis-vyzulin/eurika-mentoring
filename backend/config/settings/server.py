from .base import *
from os import environ as env


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get('DJANGO_SECRET_KEY', 'django-insecure-(d79$wx1^3g81p=1j$s9&i4(48^q*7*c6dl%e)q^-m9+579h5$')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get('DJANGO_DEBUG', True)
ALLOWED_HOSTS = env.get('DJANGO_ALLOWED_HOSTS', 'localhost 0.0.0.0 127.0.0.1').split(' ')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.get('POSTGRES_NAME', 'postgres'),
        'USER': env.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': env.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': 'database',
        'PORT': '5432',
    }
}

# Model of Users
AUTH_USER_MODEL = 'evrika.User'


# Corsheaders settings
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'https://127.0.0.1:8080',
    'https://127.0.0.1:8000',
)
