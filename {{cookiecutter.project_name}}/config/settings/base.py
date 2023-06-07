import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = int(env('DEBUG', default=0))

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS').split(' ')

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'drf_spectacular_sidecar',
    'drf_spectacular',
    'email_from_template',
    # Custom apps
    'apps.core',
    {%- if cookiecutter.add_example_apps == 'True' %}
    'apps.auth',
    'apps.users',
    'apps.todo',
    {% endif -%}
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apps.core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

ASGI_APPLICATION = 'config.asgi.application'

COMMON_PASSWORDS_FILE = os.path.join(BASE_DIR, 'config',
                                     'common_passwords.txt.gz')

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa: 501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # noqa: 501
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # noqa: 501
        'OPTIONS': {
            'password_list_path': COMMON_PASSWORDS_FILE,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # noqa: 501
    },
    {
        'NAME': 'zxcvbn_password.ZXCVBNValidator',
        'OPTIONS': {
            'min_score': 3,
            'user_attributes': ('username', 'email', 'first_name', 'last_name')
        }
    }
]

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en-us', 'English'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': '{{cookiecutter.project_name}} API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}
{% if cookiecutter.add_example_apps == 'True' %}
AUTH_USER_MODEL = 'users.CustomUser'
{% endif %}
