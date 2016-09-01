from django.db import models

# Create your models here. Manager.py makemigrations
from django.forms import ModelForm


class Formulario(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    rg = models.CharField(max_length=255)
    nascimento = models.DateField()
    sexo = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    #Address
    cep = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

class FormularioForm(ModelForm):
    class Meta:
        model = Formulario
        fields = ['email','senha','nome', 'sobrenome', 'cpf', 'rg', 'nascimento', 'sexo', 'telefone', 'celular', 'cep', 'rua', 'numero', 'complemento'
                  , 'bairro', 'cidade', 'estado']
