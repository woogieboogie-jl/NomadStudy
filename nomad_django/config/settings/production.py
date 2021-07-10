"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('RDS_NAME'),
    'HOST': os.environ.get('RDS_HOST'),
    'USER': os.environ.get('RDS_USER'),
    'PASSWORD': os.environ.get('RDS_PASSWORD'),
    'PORT': os.environ.get('RDS_PORT'),
    }
}

ALLOWED_HOSTS = [
    '.woogieboogie.dev'
    'nomad-django.eba-i7hwiw2c.ap-northeast-2.elasticbeanstalk.com',
    '3.35.206.190',
    '13.124.101.71',
    '3.37.90.31',
    ]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

AWS_STORAGE_BUCKET_NAME = "nomad-django-production-bucket"
AWS_LOCATION = 'static'
AWS_REGION = 'ap-northeast-2'
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com"

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")


sentry_sdk.init(
    dsn=os.environ.get("SENTRY_URL"),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
    )