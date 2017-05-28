class DevOverridableMixin(object):
    """
    This mixin is used for overriable settings for Development.
    The reason this settings aren't in Development is that they otherwise
    wouldn't be overridable with LocalSettings. Hence, this contains all
    settings that are allowed to be overriden in Development.
    """
    DEBUG = True

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    SECRET_KEY = 'j)^^qqe06itokac=3mwd&yw^wrx&jh!zye@*8+%i!m5uiybe09'
    ALLOWED_HOSTS = ['*']
