# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=255)),
                ('rg', models.CharField(max_length=255)),
                ('nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('celular', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
                ('complemento', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
            ],
        ),
    ]
