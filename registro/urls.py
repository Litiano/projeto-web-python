from django.conf.urls import url

from registro import views

urlpatterns = [
    url(r'^cadastro/', views.formulario, name='formulario'),
    url(r'^cadastroPost', views.formularioPost, name='formularioPost'),
    url(r'^listar', views.listar, name='listar'),
    url(r'^editar/([0-9]*)/$', views.editar, name='editar'),
    url(r'^excluir/([0-9]*)/$', views.excluir, name='excluir'),
]
