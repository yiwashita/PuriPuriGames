"""
WSGI config for ppg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/

Web Server Gateway Interface の設定（通常の Web アプリ用）
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ppg.settings')

application = get_wsgi_application()
