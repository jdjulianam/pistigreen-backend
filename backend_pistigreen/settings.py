from datetime import timedelta
from pathlib import Path
import environ
import os
import dj_database_url
from decouple import config

# Inicializar la instancia de environ
env_parser = environ.Env()


# Definir la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')

# Leer el archivo .env adecuado
if DJANGO_ENV == 'production':
    environ.Env.read_env('.env.production')
else:
    environ.Env.read_env('.env.development')


# Configurar las variables de entorno
DEBUG = env_parser.bool("DEBUG", default=False)
SECRET_KEY = env_parser("SECRET_KEY")
ALLOWED_HOSTS = env_parser.list("ALLOWED_HOSTS")
CORS_ALLOWED_ORIGINS = env_parser.list("CORS_ALLOWED_ORIGINS")
CSRF_TRUSTED_ORIGINS = env_parser.list("CSRF_TRUSTED_ORIGINS")
WEBSITE_URL = env_parser("WEBSITE_URL")

EMAIL_BACKEND = env_parser("EMAIL_BACKEND")
if EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend":
    EMAIL_HOST = env_parser("EMAIL_HOST")
    EMAIL_PORT = env_parser("EMAIL_PORT")
    EMAIL_USE_TLS = env_parser.bool("EMAIL_USE_TLS", default=True)
    EMAIL_HOST_USER = env_parser("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env_parser("EMAIL_HOST_PASSWORD")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES['default'] = dj_database_url.config()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'post',
    'search',
    'notification',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_pistigreen.urls'

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

WSGI_APPLICATION = 'backend_pistigreen.wsgi.application'

AUTH_USER_MODEL = 'account.User'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=env_parser.int('ACCESS_TOKEN_LIFETIME', 30)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=env_parser.int('REFRESH_TOKEN_LIFETIME', 180)),
    'ROTATE_REFRESH_TOKENS': env_parser.bool('ROTATE_REFRESH_TOKENS', False),
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración específica de seguridad para producción
if DJANGO_ENV == 'production':
    SECURE_SSL_REDIRECT = env_parser.bool('SECURE_SSL_REDIRECT', True)
    SESSION_COOKIE_SECURE = env_parser.bool('SESSION_COOKIE_SECURE', True)
    CSRF_COOKIE_SECURE = env_parser.bool('CSRF_COOKIE_SECURE', True)
    SECURE_BROWSER_XSS_FILTER = env_parser.bool('SECURE_BROWSER_XSS_FILTER', True)
    SECURE_CONTENT_TYPE_NOSNIFF = env_parser.bool('SECURE_CONTENT_TYPE_NOSNIFF', True)
    X_FRAME_OPTIONS = env_parser("X_FRAME_OPTIONS", default="DENY")

