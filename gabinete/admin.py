from django.contrib import admin
from .models import *


class UsuarioAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('user', 'deputado')
    list_filter = ('deputado',)


class DeputadoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Deputado, DeputadoAdmin)