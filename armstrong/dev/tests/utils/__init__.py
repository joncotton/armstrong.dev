from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

from .base import ArmstrongTestCase, override_settings