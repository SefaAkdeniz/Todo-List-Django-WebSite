from django.contrib import admin
from . import models

class ListAdmin(admin.ModelAdmin):
    list_display = ('name','user')
    list_display_links = ('name','user')
    list_filter = ('name','user')
    list_per_page = 10

class ListItemAdmin(admin.ModelAdmin):
    list_display = ('name','deadline','createdDate','status')
    list_display_links = ('name','deadline','createdDate','status')
    list_filter = ('name','deadline','createdDate','status')
    list_per_page = 10

# Register your models here.

admin.site.register(models.List,ListAdmin)
admin.site.register(models.ListItem,ListItemAdmin)