from django.conf.urls import url

from autenticacao import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^loginPost/', views.loginPost, name='loginPost'),
]
