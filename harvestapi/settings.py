# Django settings for harvestapi project.
import os

#Use the following live settings to build on Travis CI
if os.getenv('BUILD_ON_TRAVIS', None):
    SECRET_KEY = "SecretKeyForUseOnTravis"
    DEBUG = False
    TEMPLATE_DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travis_ci_test',                      
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '127.0.0.1'
        }
    }
else:
    #import the settings specific to the environment (dev or live)

    # Helper lambda for gracefully degrading environmental variables:
    env = lambda e, d: environ[e] if environ.has_key(e) else d

    DEBUG = bool(os.environ['DEBUG'])
    TEMPLATE_DEBUG = bool(os.environ['TEMPLATE_DEBUG'])

    ADMINS = (
        # ('Your Name', 'your_email@example.com'],
    )

    MANAGERS = ADMINS

    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ['.herokuapp.com']

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = os.environ['TIME_ZONE']

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = os.environ['LANGUAGE_CODE']

    SITE_ID = int(os.environ['SITE_ID'])

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = bool(os.environ['USE_I18N'])

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = bool(os.environ['USE_L10N'])

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = bool(os.environ['USE_TZ'])

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/var/www/example.com/media/"
    MEDIA_ROOT = os.environ['MEDIA_ROOT']

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://example.com/media/", "http://media.example.com/"
    MEDIA_URL = os.environ['MEDIA_URL']


    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = os.environ['SECRET_KEY']

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
#        'password_policies.middleware.PasswordChangeMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = os.environ['ROOT_URLCONF']

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = os.environ['WSGI_APPLICATION']

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),

    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        # 'rest_framework.authtoken',
        'farmers',
        'rest_framework_swagger',
        'registration',
        'django.contrib.humanize',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        'django_filters',
        'widget_tweaks',
#        'password_policies',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
    )

    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

    #added for Heroku
    # Parse database configuration from $DATABASE_URL
    import dj_database_url

    DATABASES = {'default': dj_database_url.config(default="'" + os.environ['DATABASE_URL'] + "'")}


    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


    # Static asset configuration
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(PROJECT_PATH, 'static'),
    )

    #pagination for API
    REST_FRAMEWORK = {
        'PAGINATE_BY': 10, #API defaults to 10 return results
        'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
        'MAX_PAGINATE_BY': 100,             # Maximum limit allowed when using `?page_size=xxx`.
        'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        )
    }

    ACCOUNT_ACTIVATION_DAYS = int(os.environ['ACCOUNT_ACTIVATION_DAYS'])

    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
    EMAIL_PORT = int(os.environ['EMAIL_PORT'])
    EMAIL_USE_TLS = bool(os.environ['EMAIL_USE_TLS'])
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    DEFAULT_FROM_EMAIL = os.environ['EMAIL_SENDER']

    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/

    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    PASSWORD_RESET_TIMEOUT_DAYS = int(os.environ['PASSWORD_RESET_TIMEOUT_DAYS'])

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'
