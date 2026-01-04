"""
ASGI config for ppg project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/

Asynchronous Server Gateway Interface の設定（非同期処理用）
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ppg.settings')

application = get_asgi_application()
