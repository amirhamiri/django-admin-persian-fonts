# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.cache import cache, caches


def app_cache():
    return caches["admin_persian"] if "admin_persian" in settings.CACHES else cache


def del_cached_active_font():
    app_cache().delete("admin_persian_font")


def get_cached_active_font():
    return app_cache().get("admin_persian_font", None)


def set_cached_active_font(font):
    app_cache().set("admin_persian_font", font)
