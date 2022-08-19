import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.erp import Type

t = Type()
t.nome = 'presinte'
t.save()