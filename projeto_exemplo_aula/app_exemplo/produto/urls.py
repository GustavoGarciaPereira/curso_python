from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('produto/<int:pk>/', views.produto_detail, name='produto_detail'),
    path('produto/novo/', views.produto_create, name='produto_create'),
    path('produto/<int:pk>/editar/', views.produto_edit, name='produto_edit'),
    path('produto/<int:pk>/excluir/', views.produto_delete, name='produto_delete'),
]
