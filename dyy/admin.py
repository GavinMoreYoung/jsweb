from django.contrib import admin

from dyy.models import *

class Dyadmin(admin.ModelAdmin):
    list_display = ['id','dyclass','dybt','dydz','dytp']
    ordering = ['id']

class Wzadmin(admin.ModelAdmin):
    list_display = ['id', 'wzbt',  'wznr']
    ordering = ['id']

admin.site.register(Dy,Dyadmin)
admin.site.register(DyClass)
admin.site.register(Wz,Wzadmin)