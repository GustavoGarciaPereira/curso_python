from . import views
from django.urls import path

urlpatterns = [
    path('cadastro/', views.index, name='cadastro'),
]