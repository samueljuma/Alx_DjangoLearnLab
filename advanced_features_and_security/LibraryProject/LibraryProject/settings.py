"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!s_uo^)v#1)x83#hnd*cobphff^an-vc(-1!y3k=z=bc3#2mag"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Security Headers
# Enables X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

# Prevents clickjacking
X_FRAME_OPTIONS = "DENY"

# Prevents MIME sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True 

# Use HTTPS Secure Cookies
# Ensures CSRF cookie is sent over HTTPS
CSRF_COOKIE_SECURE = True 

# Ensures session cookies are sent over HTTPS
SESSION_COOKIE_SECURE = True  

# Redirect to HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bookshelf",
    "relationship_app",
    "csp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "LibraryProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates",],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LibraryProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "bookshelf.CustomUser"


CSP_DEFAULT_SRC = ("'self'",)  # Only allow content from our domain
CSP_SCRIPT_SRC = ("'self'", "https://trusted-cdn.com")  # Allow scripts from trusted CDN
CSP_STYLE_SRC = ("'self'", "https://trusted-cdn.com")  # Allow CSS from trusted CDN
CSP_IMG_SRC = ("'self'", "data:", "https://trusted-image-host.com")  # Allow images
CSP_FONT_SRC = ("'self'", "https://trusted-fonts.com")  # Allow fonts
CSP_FRAME_ANCESTORS = ("'none'",)  # Prevent iframe embedding

# Force HTTPS redirect
# Redirects all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  

# HTTP Strict Transport Security (HSTS)
# Enable HSTS for 1 year
SECURE_HSTS_SECONDS = 31536000 

# Apply HSTS to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True 

# Enable HSTS preload list
SECURE_HSTS_PRELOAD = True 

SECURE_REDIRECT_EXEMPT = [] # List of URL prefixes that are exempt from HTTPS redirect


"""
    Setting	                                Purpose
    SECURE_SSL_REDIRECT = True	            Forces HTTPS for all requests
    SECURE_HSTS_SECONDS = 31536000	        Enables HSTS for 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True	Applies HSTS to subdomains
    SECURE_HSTS_PRELOAD = True	            Allows preloading for better enforcement
    SESSION_COOKIE_SECURE = True	        Ensures session cookies are sent over HTTPS
    CSRF_COOKIE_SECURE = True	            Ensures CSRF tokens are sent over HTTPS
    X_FRAME_OPTIONS = "DENY"	            Prevents clickjacking attacks
    SECURE_CONTENT_TYPE_NOSNIFF = True	    Stops MIME-type sniffing
    SECURE_BROWSER_XSS_FILTER = True	    Enables browser's XSS protection
"""
