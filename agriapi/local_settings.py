
DEBUG = False 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'harvest_api',
        'USER': 'harvest_api_user',
        'HOST': 'localhost',
        'PASSWORD': 'harvest',
        'PORT': '',
    }
}
#test email
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025


