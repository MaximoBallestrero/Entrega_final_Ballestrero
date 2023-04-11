from django.contrib import admin

from usuarios.models import Avatar, DescripcionUsuario
# Register your models here.
admin.site.register(Avatar)
admin.site.register(DescripcionUsuario)