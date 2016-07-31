#Projeto de MATC84 - LABORATÓRIO DE PROGRAMAÇÃO WEB

##Instruções para configurar o ambiente com Python e Django

1 - Instalar o Python - https://www.python.org/downloads/

2 - Instalar o PIP - https://pip.pypa.io/en/stable/installing/

2.1 - Download do PIP https://bootstrap.pypa.io/get-pip.py

2.2 - $ python get-pip.py

3 - Instalar o VirtualEnv

3.1 - $ pip install virtualenvwrapper, para windows utilize virtualenvwrapper-win

4 - Criar o ambiente virtual

4.1 - $ mkvirtualenv NOME_DO_AMBIENTE

# Se mkvirtualenv não funcionar, tente isso:

$ export WORKON_HOME=~/Envs

$ mkdir -p $WORKON_HOME

$ source /usr/local/bin/virtualenvwrapper.sh

4.2 - $ workon NOME_DO_AMBIENTE #para acessar o ambiente

5 - Instalar o Django

5.1 - $ pip install django

6 - Criar o projeto

6.1 - $ django-admin startproject MEU_PROJETO

7 - Criar o app

7.1 - $ python manage.py startapp PRIMEIRO_APP #Neste caso criamos auth e register

8 - Executar servidor

8.1 - $ python manage.py runserver 80 #pode ser outra porta