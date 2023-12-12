"""
ASGI config for python_heroku_task project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_heroku_task.settings')

app = get_asgi_app()
