from django.contrib import admin
from . import models
for name in dir(models):
    obj = getattr(models, name)
    if hasattr(obj, '__bases__') and models.models.Model in obj.__bases__:
        admin.site.register(obj)
