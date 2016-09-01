from django.shortcuts import render
from django.contrib.auth import authenticate, login
from registro.models import Formulario

def login(request):
    return render(request, 'autenticacao/login.html')

def loginPost(request):
        senha = request.POST.get('senha', '')
        email = request.POST.get('email', '')

        if Formulario.objects.filter(email=email,senha=senha):
            return render(request, 'base/index.html')
        else :
            return render(request, 'autenticacao/login.html')
