from django.contrib.messages import constants as messages
from pathlib import Path
import environ
import os

ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'localhost')]
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environ and read the .env file
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))  # Read .env file from the base directory

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')  # Make sure .env contains a valid SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)  # Read DEBUG from .env (default True for local development)

# Add allowed hosts here (you can add multiple)
# ALLOWED_HOSTS = [env('WEB_DOMAIN', default='127.0.0.1')]  # Default to localhost if not set in .env
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ALLOWED_HOSTS = ['voteonline-f96v.onrender.com']


# Application definition
INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'accounts/templates', BASE_DIR / 'users/templates'],
        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# For development use:
STATIC_URL = '/static/'

# Where your static files are placed in your app for development
STATICFILES_DIRS = [BASE_DIR / 'static']

# For production (collectstatic command will place files here)
STATIC_ROOT = BASE_DIR / 'staticfiles'  # make sure it's a different folder


MEDIA_URL = '/mediaFiles/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Message tags to customize error messages display
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Security Settings (Disable SSL for development)
SECURE_SSL_REDIRECT = False  # Disable SSL redirect in development

# Enable WhiteNoise to serve static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add any other settings here as needed...
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/voter/profile/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True




