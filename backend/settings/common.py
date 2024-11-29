import os

APP_NAME = "flaskDemo"

SECRET_KEY = os.getenv('SECRET_KEY', "63K8r4xxIW1A")

ENV_FILE = './.env'
CELERY_ENV_FILE = './.env'

