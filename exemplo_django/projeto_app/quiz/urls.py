from django.urls import path
from .views import quiz

urlpatterns = [
    path('questao/',quiz, name='quiz')
]
