from django.contrib import admin
from . import models
for name in dir(models):
	obj = getattr(models, name)
	if hasattr(obj, '__bases__') and hasattr(obj, '__module__') and obj.__module__ == models.__name__:
		if hasattr(obj, '_meta') and hasattr(obj._meta, 'app_label'):
			admin.site.register(obj)
