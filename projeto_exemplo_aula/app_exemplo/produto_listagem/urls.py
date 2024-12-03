from django.urls import path
from .views import listagem_ativo, listagem_nao_ativo, reativar


urlpatterns = [
    path('ativos/',listagem_ativo),
    path('nao_ativo/',listagem_nao_ativo, name='nao_ativo'),
    path('reativar/<int:pk>/',reativar, name='reativar')
]
