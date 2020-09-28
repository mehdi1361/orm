import importlib
from django.conf import settings


def test_blog_module_exists():
    assert importlib.util.find_spec("base") is not None


def test_blog_on_install_apps():
    assert "base.apps.BaseConfig" in settings.INSTALLED_APPS
