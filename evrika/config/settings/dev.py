from .base import *
from os import environ as env


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get('DJANGO_SECRET_KEY', 'django-insecure-(d79$wx1^3g81p=1j$s9&i4(48^q*7*c6dl%e)q^-m9+579h5$')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get('DJANGO_DEBUG', True)
ALLOWED_HOSTS = env.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1 localhost").split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}