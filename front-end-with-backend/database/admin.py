from django.contrib import admin

# Register your models here.
from database.models import database


class databaseadmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'message')


admin.site.register(database, databaseadmin)
