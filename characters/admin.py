from django.contrib import admin
from .models import NPC

class NPCs(admin.ModelAdmin):
    list_display = ('id', 'nome', 'raca', 'classe', 'idade')
    list_display_links = ('id', 'nome')
    search_fields = ['id', 'nome', 'raca', 'classe']

admin.site.register(NPC, NPCs)

