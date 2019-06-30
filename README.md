# Demo Python 3 e Django
Simples aplicação web com Python 3 e Django

#### Requisitos
- **Python** >= 3.6: https://www.python.org/downloads/release/python-368/
- **Django** >= 2.1: https://docs.djangoproject.com/en/2.2/intro/install/
- **Allauth**: https://django-allauth.readthedocs.io/en/latest/installation.html

#### Iniciando Aplicação
Após realizado o clone deste repositório, inicie o terminal na pasta raiz da aplicação.
Em seguida execute:
```git
$ py manage.py runserver
```
A aplicação será executada na porta `8000` na máquina local, para acessar basta digitar a url: https://localhost:8000

#### Funcionalidades
- **Login**: para acessar a aplicação realize o login com sua conta do Facebook
- **CRUD**: o crud(create, retrivie, update e delete) é realizado no objeto Cliente, juntamente com seu Endereço e Telefone.
- **ViaCEP**: no cadastro/update os campos correspondentes ao Endereço são preenchidos automaticamente conforme a pesquisa do CEP é realizada na API ViaCEP (https://viacep.com.br/)
- **GMaps**: no cadastro após a busca do Endereço é exibido o mesmo em um pequeno Mapa na página de cadastro.

#### Acesso Admin
Para ter acesso as funcionalidades de administrador da aplicação basta digitar a url https://localhost:8000/admin e realizar o login com as credenciais (Usuário: admin, Senha: admin123)
