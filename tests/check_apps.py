import importlib
from django.conf import settings


def test_base_module_exists():
    assert importlib.util.find_spec("base") is not None


def test_base_on_install_apps():
    assert "base.apps.BaseConfig" in settings.INSTALLED_APPS
