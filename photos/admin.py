from django.contrib import admin
from .models import Galeria

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'owner']
    list_filter = ['owner']
    # autocomplete_fields = ["slug"]
admin.site.register (Galeria, GaleriaAdmin)
