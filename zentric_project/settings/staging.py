from .base import *
from decouple import config


ALLOWED_HOSTS = ['your-staging-domain.com']

# Configuración de base de datos para staging (por ejemplo, PostgreSQL)
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


