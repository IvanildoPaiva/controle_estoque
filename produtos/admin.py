from django.contrib import admin
from .models import Produto

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_disply = ('nome', 'preco', 'quantidade')
    list_filter = ('nome',)
    search_fields = ('nome',)
admin.site.register(Produto, ProdutoAdmin)