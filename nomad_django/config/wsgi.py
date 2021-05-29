"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""


import os

from django.core.wsgi import get_wsgi_application
print(os.environ.get('ENVIRONMENT'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"config.settings.{os.environ.get('ENVIRONMENT')}")
application = get_wsgi_application()
