from __future__ import absolute_import

import os

from willsnetwork.settings.base import Base
from willsnetwork.settings.mixins import DevOverridableMixin

try:
    from willsnetwork.settings.local import LocalSettings
except ImportError:
    class LocalSettings(object):
        pass


class Development(LocalSettings, DevOverridableMixin, Base):
    """
    These are the settings for Development environment

    Development settings can be overridden by creating your own
    `willsnetwork.settings.local.LocalSettings object`. Note that only the
    settings in DevOverridableMixin can be overridden like so.
    """

    PROJECT_PATH = os.path.realpath(
        os.path.join(os.path.dirname(__file__), '..', '..', '..'))
