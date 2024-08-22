from django.shortcuts import render, get_object_or_404, redirect
from .models import Adocao
from .forms import AdotarAnimalForm



def adotar_animal(request):
    if request.method == 'POST':
        form = AdotarAnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_adocoes')  
    else:
        form = AdotarAnimalForm()
    
    return render(request, 'adotar_animal.html', {
        'form': form,
    })

def listar_adocoes(request):
    adocoes = Adocao.objects.all()
    return render(request, 'listar_adocoes.html', {'adocoes': adocoes,})


def adotar(request, id):
    animal = get_object_or_404(Adocao, id=id)
    return render(request, 'adotar.html', {'animal': animal})

def editar_adocao(request, pk):
    adocao = get_object_or_404(Adocao, pk=pk)
    
    if request.method == 'POST':
        form = AdotarAnimalForm(request.POST, instance=adocao)
        if form.is_valid():
            form.save()
            return redirect('listar_adocoes')
    else:
        form = AdotarAnimalForm(instance=adocao)

    return render(request, 'editar_adocoes.html', {
        'form': form,
        'adocao': adocao,
    })


def deletar_adocao(request, pk):
    adocao = get_object_or_404(Adocao, pk=pk)
    adocao.delete()
    return redirect('listar_adocoes')


