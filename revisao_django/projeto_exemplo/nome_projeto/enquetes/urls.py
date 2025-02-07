from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('', views.lista_enquetes, name='lista'),
    path('<int:enquete_id>/', views.detalhes_enquete, name='detalhes'),
    path('<int:enquete_id>/votar/', views.votar, name='votar'),
    path('<int:enquete_id>/resultados/', views.resultados, name='resultados'),
]