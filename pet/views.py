from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnimalForm
from .models import Animal
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.urls import reverse
from adote.forms import AdotarAnimalForm
from donations.models import Doacao
from comentarios.models import Comentario
from adote.models import Adocao
from denuncia.models import Denuncia



@login_required
def create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin'))
    else:
        form = AnimalForm()
    return render(request, 'formCreate.html', {'form': form})


@login_required
def readall(request):
    animais = Animal.objects.all()
    first_animal = animais.first() if animais.exists() else None
    return render(request, "index.html", {'animais': animais, 'animal': first_animal})


@login_required
def read(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'user_detail.html', {'animal': animal})


@login_required
def update(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('admin')  
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'formupdate.html', {'form': form, 'animal': animal})


@login_required
def delete(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    if request.method == 'POST':
        animal.delete()
        return HttpResponseRedirect(reverse('admin'))
    
    return render(request, 'confirmdelete.html', {'animal': animal})


@login_required
def confirmdelete(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    return render(request, 'confirmdelete.html', {'animal': animal})


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    animais = Animal.objects.all()
    return render(request, 'index.html', {'animais': animais})


def user_index(request):
    animais = Animal.objects.all()
    return render(request, 'index.html', {'animais': animais})


def user_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    if request.method == 'POST':
        form = AdotarAnimalForm(request.POST)
        if form.is_valid():
            adotado = form.save(commit=False)
            adotado.animal = animal
            adotado.save()
            return redirect('listar_adocoes')
    else:
        form = AdotarAnimalForm()
    return render(request, 'user_detail.html', {'animal': animal, 'form': form})





@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def veterinarian(request):
    animais = Animal.objects.all()
    return render(request, 'vet.html', {'animais': animais})


@login_required
def services(request):
    return render(request, 'services.html')


@login_required
def gallery(request):
    animais = Animal.objects.all()
    return render(request, 'gallery.html', {'animais': animais})


@login_required
def admin(request):
    animais = Animal.objects.all()
    adocoes = Adocao.objects.all()
    return render(request, 'blog.html', {'animais': animais, 'adocoes': adocoes})


@login_required
def pricing(request):
    comentarios = Comentario.objects.all()
    denuncias = Denuncia.objects.filter(denunciante=request.user)
    return render(request, 'pricing.html', {'comentarios': comentarios, 'denuncias': denuncias})


@login_required
def blog(request):
    return render(request, 'blog.html')


@login_required
def contact(request):
    doacao = Doacao.objects.filter(doador=request.user)
    return render(request, 'contact.html', {'doacao': doacao})












@login_required
def apadrinhamento_detalhes(request, animal_id):
    user = request.user
    animal = get_object_or_404(Animal, id=animal_id)
    context = {
        'user': user,
        'animal': animal
    }
    return render(request, 'pet/apadrinhar.html', context)

def apadrinhar_view(request, animal_id):
    if request.method == 'POST':
        animal = get_object_or_404(Animal, id=animal_id)
        
        return JsonResponse({'message': 'O animal foi apadrinhado, entraremos em contato'})
    return JsonResponse({'error': 'Requisição inválida'}, status=400)


