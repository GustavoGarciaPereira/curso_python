from django.contrib import admin

from .models import Enquete, Opcao

class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 3  # 3 opções por padrão

@admin.register(Enquete)
class EnqueteAdmin(admin.ModelAdmin):
    inlines = [OpcaoInline]
    list_display = ['pergunta', 'data_publicacao']

@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ['texto_opcao', 'votos']