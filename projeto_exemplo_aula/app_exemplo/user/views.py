from django.shortcuts import render
from produto.models import Produto
# Create your views here.
def index(request):
    pro = Produto.objects.all().order_by('-preco')

    return render(request,'main.html',{"produto":pro})