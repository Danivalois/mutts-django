# settings.py
import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key
from django.shortcuts import render
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "%j8e&1_gf_t*dpp)j@stuzd=r+(^yy71(z+&6l@551137ugxur"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".vercel.app",
    os.getenv("VERCEL_URL", ""),  # Dynamically get Vercel's deployment URL
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # Supabase default database name
        'USER': 'postgres',  # Supabase default user
        'PASSWORD': '2h.8QG38Uba_g@w',  # Your Supabase password
        'HOST': 'mfusnfwxtnzzbmalklqw.supabase.co',  # Your Supabase database host
        'PORT': '5432',  # Default PostgreSQL port
    }
}




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')





SECRET_KEY = get_random_secret_key()

CSRF_TRUSTED_ORIGINS = [
    "https://mutts-django.vercel.app",
    "https://*.vercel.app"
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

ROOT_URLCONF = 'mutts.urls'  # ✅ Ensure this exists!

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

TIME_ZONE = "America/Sao_Paulo"
USE_TZ = True


#pages customized

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Make sure your templates are inside the 'templates' folder
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


