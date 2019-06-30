from django.shortcuts import render, redirect
from demo.models import Cliente, Endereco, Telefone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


# Retorna uma lista com todos os clientes cadastrados
@login_required(login_url='/')
def index(request):
    clientes = Cliente.objetos.all()
    template_name = 'clientes.html'
    context = {
        'clientes': clientes
    }
    return render(request, template_name, context)

# Retorna a página de cadastro de clientes
@login_required(login_url='/')
def form_cadastro(request):
    template_name = 'registro.html'
    return render(request, template_name)

# Cadastrando um cliente
@login_required(login_url='/')
def create_cliente(request):
    data = {}
    if(request.method == 'POST'):
        data = request.POST

    cli = Cliente()
    tel = Telefone()
    end = Endereco()

    if(data.get('cli_id')):
        cli.id = data.get('cli_id')
        tel.id = data.get('tel_id')
        end.id = data.get('end_id')

    tel.numero = data.get('tel')
    tel.save()

    end.cep = data.get('cep')
    end.rua = data.get('rua')
    end.num = data.get('num')
    end.bairro = data.get('bairro')
    end.cidade = data.get('cidade')
    end.uf = data.get('uf')
    end.pais = data.get('pais')
    end.save()

    cli.nome = data.get('nome')
    if(data.get('cli_id')):
        cli.telefone = tel
        cli.endereco = end
    else:
        cli.telefone = Telefone.objetos.last()
        cli.endereco = Endereco.objetos.last()
    cli.save()

    return redirect('website:index')

# Removendo um cliente
@login_required(login_url='/')
def delete_cliente(request, id):
    cli = Cliente.objetos.get(id=id)
    cli.endereco.delete()
    cli.telefone.delete()
    cli.delete()
    return redirect('website:index')

# Atualizando um cliente
@login_required(login_url='/')
def update_cliente(request, id):
    cli = Cliente.objetos.get(id=id)
    print(cli.nome)
    template_name = 'atualizar.html'
    return render(request, template_name, {'cliente': cli})

# Deslogando da aplicação
@login_required(login_url='/')
def logout(request):
    auth_logout(request)
    return redirect('/')
