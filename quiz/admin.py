from django.contrib import admin

# Register your models here.
from .models import Categoria, Questao

admin.site.register(Categoria)
admin.site.register(Questao)