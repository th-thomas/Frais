from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_%$qy=(_-$5)dv-dl^b1+p$)^o3la+x2s=gwqwb-s9qpzs2w90'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Adresses auxquelles le site est accessible
# Exemple : ['localhost', 'exempledesite.abc', '123.456.123.789']
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gsbdb',
        'USER': 'gsbuser',
        'PASSWORD': 'gsbpwd',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
# Django placera les fichiers statiques dans ce répertoire
# afin que Nginx puisse traiter les requêtes pour ces éléments
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')

