from django.urls import path
from django.contrib.auth import views as auth_views

# Importando a função index definida no arquivo views.py
from . import views

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET/
    path('', views.index, name='index'),    
    path('form_cadastro', views.form_cadastro, name='form_cadastro'), 
    path('create_cliente', views.create_cliente, name='create_cliente'),
    path('delete_cliente/<int:id>', views.delete_cliente, name='delete_cliente'),
    path('update_cliente/<int:id>', views.update_cliente, name='update_cliente'),
    path('logout', views.logout, name='logout'),
]