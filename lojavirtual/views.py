from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from . models import Produto
from . forms import ProdutoForm

# Create your views here.

def home(request):
    lista_produto = Produto.objects.all()
    return render(request, 'index.html', {'lista_produto':lista_produto})

def produto(request, slug):
    produto = get_object_or_404(Produto, slug=slug)

    return render(request, 'produto.html', {'produto':produto})

def carinho(request):
    return render(request, 'carinho.html')


def produtos_api(request):
    produtos = Produto.objects.filter(disponivel=True)
    return JsonResponse({
        'produtos': [
            {
                'id': produto.slug,
                'nome': produto.titulo,
                'preco': str(produto.preco),
                'imagem': produto.foto.url if produto.foto else '',
            }
            for produto in produtos
        ]
    })


def cadastro_produto(request):

    if request.method == 'POST':
         form = ProdutoForm()
         
   

    return render(request, 'cadastro.html', {'form': form })




