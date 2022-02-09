from django.contrib import admin

from spacejam import models

admin.site.register(models.Space, admin.ModelAdmin)
