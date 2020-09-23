"""
WSGI config for bnaPager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""


## for other servers
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bnaPager.settings')

# application = get_wsgi_application()

##for heroku

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bnaPager.settings')
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)