"""
WSGI config for studio_reservation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from pathlib import Path
import environ

# ******* Reading Project Environment *******
ENV_FILE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
env.read_env(env_file=os.path.join(ENV_FILE_DIR, '.env'))

if env.bool('IS_PRODUCTION', default='') == True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studio_reservation.settings.production')
elif env.bool('IS_PRODUCTION', default='') == False and env.bool('IS_STAGING', default='') == True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studio_reservation.settings.staging')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studio_reservation.settings.development')

application = get_wsgi_application()
