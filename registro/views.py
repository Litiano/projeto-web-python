from glob import escape

from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from registro.models import Formulario, FormularioForm


def formulario(request):
    return render(request, 'registro/formulario.html')

def formularioPost(request):
    post = request.POST
    form = Formulario()
    form.nome = post.get('nome', '')
    form.sobrenome = post.get('sobrenome', '')
    form.cpf = post.get('cpf', '')
    form.rg = post.get('rg', '')
    nascimento = post.get('nascimento', '').split("/")
    form.nascimento = nascimento[2] + '-' + nascimento[1] + '-' + nascimento[0]
    form.sexo = post.get('sexo', '')
    form.telefone = post.get('telefone', '')
    form.celular = post.get('celular', '')
    form.cep = post.get('cep', '')
    form.rua = post.get('rua', '')
    form.numero = post.get('numero', '')
    form.complemento = post.get('complemento', '')
    form.bairro = post.get('bairro', '')
    form.cidade = post.get('cidade', '')
    form.estado = post.get('estado', '')
    form.save()
    return HttpResponse('FOI')