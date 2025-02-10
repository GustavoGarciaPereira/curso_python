from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Enquete, Opcao

def lista_enquetes(request):
    enquetes = Enquete.objects.all()
    return render(request, 'enquetes/lista.html', {'enquetes': enquetes})

def detalhes_enquete(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    return render(request, 'enquetes/votar.html', {'enquete': enquete})

def votar(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    try:
        opcao_selecionada = enquete.opcoes.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'enquetes/votar.html', {
            'enquete': enquete,
            'error_message': "Selecione uma opção válida."
        })
    else:
        opcao_selecionada.votos += 1
        opcao_selecionada.save()
        return redirect('enquetes:resultados', enquete_id=enquete.id)

def resultados(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    return render(request, 'enquetes/resultados.html', {'enquete': enquete})