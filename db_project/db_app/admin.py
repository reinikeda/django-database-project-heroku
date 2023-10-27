from django.contrib import admin
from . import models


class TastAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'due_date', 'is_completed')


admin.site.register(models.Task, TastAdmin)