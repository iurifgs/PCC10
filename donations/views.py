from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doacao
from usuario.models import Usuario
from .forms import DonationForm
from django.core.mail import send_mail
from django.conf import settings


@login_required
def donation_create(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            doacao = form.save(commit=False)

            try:
                # Obtendo a instância do modelo Usuario correspondente ao usuário atual
                usuario = Usuario.objects.get(user=request.user)
            except Usuario.DoesNotExist:
                # Se não encontrar um perfil para o usuário, redirecione para uma página de erro
                # ou crie um novo perfil para o usuário. Aqui estamos redirecionando para 'contact'
                return redirect('contact')

            doacao.doador = usuario
            doacao.save()
            
            send_mail(
                'Obrigado por sua doação!',
                f'Obrigado por doar {doacao.quantia}. Sua generosidade é apreciada.',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            return redirect('contact')
    else:
        form = DonationForm()
    
    return render(request, 'donation_form.html', {'form': form})



@login_required
def donation_update(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    if request.method == 'POST':
        form = DonationForm(request.POST, instance=doacao)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = DonationForm(instance=doacao)
    return render(request, 'donation_form.html', {'form': form})



@login_required
def donation_delete(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    if request.method == 'POST':
        doacao.delete()
        return redirect('contact')
    return render(request, 'donation_confirm_delete.html', {'doacao': doacao})



