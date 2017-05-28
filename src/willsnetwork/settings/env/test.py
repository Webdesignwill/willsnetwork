from __future__ import absolute_import

from willsnetwork.settings.env.development import Development


class Test(Development):
    """
    These are the settings for Test environment
    """

    RUNNING_TESTS = True
    LANGUAGE_CODE = 'en'  # use English in the tests

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_database',
        }
    }
