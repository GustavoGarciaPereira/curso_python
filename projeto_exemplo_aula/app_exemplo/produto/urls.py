from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('produto/<int:pk>/', views.produto_detail, name='produto_detail'),
    path('produto/novo/', views.produto_create, name='produto_create'),
    path('produto/<int:pk>/editar/', views.produto_edit, name='produto_edit'),
    path('produto/<int:pk>/excluir/', views.produto_delete, name='produto_delete'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
