# settings.py
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "%j8e&1_gf_t*dpp)j@stuzd=r+(^yy71(z+&6l@551137ugxur"
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "mutts-django.vercel.app",
    "mutts-django-kg33f8f9c-dani-valois-projects.vercel.app",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



#'DIRS': [WindowsPath('C:/Users/apln2/Dropbox/Mutts_Website/mutts_django/templates')],


# Define BASE_DIR at the beginning
BASE_DIR = Path(__file__).resolve().parent.parent
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  
STATICFILES_DIRS = [BASE_DIR / "static"]  # ✅ Add this to find static files
STATIC_ROOT = BASE_DIR / "staticfiles"  # ✅ Required for collectstatic


DEBUG = False  # ✅ Keep True for debugging. Change to False for production.

ALLOWED_HOSTS = [
    "127.0.0.1", 
    "localhost", 
    "lojinhamutts.vercel.app",
]

ROOT_URLCONF = 'mutts.urls'  # ✅ This should be here!



BASE_DIR = Path(__file__).resolve().parent.parent  # ✅ Defines the base directory

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # ✅ Tell Django where templates are
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




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # ✅ Add your apps here
    'products',
    'customers',
    'orders',
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # ✅ REQUIRED
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ✅ REQUIRED
    'django.contrib.messages.middleware.MessageMiddleware',  # ✅ REQUIRED
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # ✅ Ensures SQLite is used
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


ALLOWED_HOSTS = [
    '127.0.0.1',  # ✅ Allow localhost access
    'localhost',   # ✅ Ensure local development works
    'lojinhamutts.vercel.app',  # ✅ Allow your Vercel domain
]

ROOT_URLCONF = 'mutts.urls'  # ✅ Ensure this exists!

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

TIME_ZONE = "America/Sao_Paulo"
USE_TZ = True

