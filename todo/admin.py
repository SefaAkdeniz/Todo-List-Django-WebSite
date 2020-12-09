from django.contrib import admin
from . import models

class ListAdmin(admin.ModelAdmin):
    list_display = ('listName','user')
    list_display_links = ('listName','user')
    list_filter = ('listName','listName')
    list_per_page = 10

# Register your models here.

admin.site.register(models.List,ListAdmin)