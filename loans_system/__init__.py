# loans_system/__init__.py
from __future__ import absolute_import, unicode_literals

from .celery import celery_app as celery_app

__all__ = ('celery_app',)
