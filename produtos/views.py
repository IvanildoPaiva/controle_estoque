from django.shortcuts import render
from .models import Produto
def lista_produtos(request):
    #select * from Produtos
    
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})