from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produto/<slug:slug>', views.produto, name='produto'),
    path('carinho/', views.carinho, name='carinho'),
    path('api/produtos/', views.produtos_api, name='produtos_api'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto')

   
]
