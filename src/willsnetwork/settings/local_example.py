class LocalSettings(object):
    """
    This is an example of LocalSettings.
    You would have to place this code in willsnetwork.settings.local
    It will be a Mixin that overrides development settings in
    willsnetwork.settings.env.Development
    """

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'willsnetwork_develop',
            'USER': 'willsnetwork_develop',
            'PASSWORD': '***',
            'HOST': '127.0.0.1',
            'PORT': '',
        }
    }
