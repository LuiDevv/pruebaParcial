from django.contrib import admin

from .models import Producto

admin.site.register(Producto)
admin.site.site_title = 'Porsche'
admin.site.site_header = 'Porsche'