from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    """Registering Shop table/model to admin panel"""
    list_display = ('name', 'location')

# Register your models here.
