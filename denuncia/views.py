from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Denuncia
from .forms import DenunciaForm

@login_required
def denuncia_list(request):
    denuncias = Denuncia.objects.filter(denunciante=request.user)
    return render(request, 'denuncia_list.html', {'denuncias': denuncias})

@login_required
def denuncia_create(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.denunciante = request.user
            denuncia.save()
            return redirect('pricing')
    else:
        form = DenunciaForm()
    return render(request, 'denuncia_form.html', {'form': form})

@login_required
def denuncia_update(request, pk):
    denuncia = get_object_or_404(Denuncia, pk=pk, denunciante=request.user)
    if request.method == 'POST':
        form = DenunciaForm(request.POST, instance=denuncia)
        if form.is_valid():
            form.save()
            return redirect('pricing')
    else:
        form = DenunciaForm(instance=denuncia)
    return render(request, 'denuncia_form.html', {'form': form})

@login_required
def denuncia_delete(request, pk):
    denuncia = get_object_or_404(Denuncia, pk=pk, denunciante=request.user)
    if request.method == 'POST':
        denuncia.delete()
        return redirect('pricing')
    return render(request, 'denuncia_confirm_delete.html', {'denuncia': denuncia})