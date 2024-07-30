"""
WSGI config for zentric_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from decouple import config
from django.core.wsgi import get_wsgi_application


ENVIRONMENT = config('ENVIRONMENT') 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zentric_project.settings.'+ENVIRONMENT)

application = get_wsgi_application()
