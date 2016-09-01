from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from registro.models import Formulario
from django.contrib.auth.decorators import login_required


def formulario(request):
    return render(request, 'registro/formulario.html')

def editar(request, id):
    item = Formulario.objects.get(pk=id)
    context = {
        'item': item,
        'id': id,
    }
    return render(request, 'registro/formulario.html', context=context)


def formularioPost(request):
    post = request.POST
    id = post.get('id', '')
    if id != '':
        form = Formulario.objects.get(pk=id)
    else:
        form = Formulario()
    form.email = post.get('email', '')
    form.senha = post.get('senha', '')
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
    return HttpResponseRedirect('/registro/listar')

def listar(request):
    itens = Formulario.objects.all()
    context = {
        'itens': itens,
    }
    return render(request, 'registro/listar.html', context=context)


def excluir(request, id):
    Formulario.objects.get(pk=id).delete()
    return HttpResponseRedirect('/registro/listar')
