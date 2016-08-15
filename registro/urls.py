from django.conf.urls import url

from registro import views

urlpatterns = [
    url(r'^cadastro/', views.formulario, name='formulario'),
    url(r'^cadastroPost', views.formularioPost, name='formularioPost'),
]
