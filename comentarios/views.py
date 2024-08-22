from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from .forms import ComentarioForm
from django.core.mail import send_mail
from django.conf import settings


def criar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST, user=request.user)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.user = request.user  
            comentario.save()
            return redirect('pricing') 
    else:
        form = ComentarioForm(user=request.user)
    
    return render(request, 'criar_comentario.html', {'form': form})



def editar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('pricing')
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'editar_comentario.html', {'form': form})



def excluir_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    if request.method == 'POST':
        comentario.delete()
        return redirect('pricing')
    return render(request, 'excluir_comentario.html', {'comentario': comentario})




def contato(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.user = request.user 
            comentario.save()

            assunto = comentario.assunto
            nome = comentario.nome
            cidade = comentario.cidade
            mensagem = comentario.mensagem

            subject = 'Nova mensagem do formulário de contato'
            body = f'''
            Assunto: {assunto}
            Nome: {nome}
            Cidade: {cidade}
            
            Mensagem:
            {mensagem}
            '''
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                ['pb437254@gmail.com'],
                fail_silently=False
            )
            return redirect('obrigado')
    else:
        form = ComentarioForm()
    
    return render(request, 'contato.html', {'form': form})