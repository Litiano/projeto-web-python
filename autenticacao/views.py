from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'autenticacao/login.html')


def loginPost(request):
    senha = request.POST.get('senha', '')
    email = request.POST.get('email', '')
    # @todo criar funcao para logar