from .base import *
from decouple import config
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['your-production-domain.com']

# Configuración de base de datos para producción (por ejemplo, PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'CONN_MAX_AGE': 600,  # Mantener la conexión abierta por 10 minutos
    }
}