from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from usuarios_.machine import *
from usuarios_.models import *
from django.http.request import *

def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'dashboards.html')

def login_(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request=request, username=email, password=password)
    if user is None:
        return render(request,'index.html',{'error_messages' : 'Login invalid!'})
    login(request,user)
    return redirect('/home')

def logout_(request):
    logout(request)
    return redirect('/')

@login_required
def search(request):
    produto = request.GET.get('query')
    produtos_obtidos = []
    produto_obtido = Anuncios_obtidos()
    produto_obtido.nome='Invicta Zeus'
    produto_obtido.autor='Wellington Freitas'
    produto_obtido.preco=859.99
    produto_obtido.descricao='Relógio em perfeito estado, facilito entrega.\nEntrar em contato no whats: 9'[:100]
    produto_obtido.predicao='Verdadeiro'
    produto_obtido.percentual = 75.0
    produto_obtido.link = 'https://pa.olx.com.br/regiao-de-belem/bijouteria-relogios-e-acessorios/invicta-yakuza-652337271?xtmc=rel%C3%B3gio+invicta&xtnp=2&xtcr=35'[:30]
        
    produto_obtido_2 = Anuncios_obtidos()
    produto_obtido_2.nome='Zeus primeira linha'
    produto_obtido_2.autor='Éverton Silva'
    produto_obtido_2.preco=99.99
    produto_obtido_2.descricao="Relógios Primeira linha AAA Premium\n\n1 Ano De Garantia ( Maquinário e Vedação ! )\nTotalmente a Prova D'água"[:100]
    produto_obtido_2.predicao='Falso'
    produto_obtido_2.percentual=100.0 
    produto_obtido_2.link='https://www.instagram.com/p/B0EimBShc2x/'[:30]

    produto_obtido_3 = Anuncios_obtidos()
    produto_obtido_3.nome='Relógio Zeus'
    produto_obtido_3.autor='Vitoria Caroline'
    produto_obtido_3.preco=109.99
    produto_obtido_3.descricao="Relogios com garantia de 6 meses todos a prova d'água de qualidade primeira linha AAA premiu todos funcionais, aceitamos cartões de crédito parcelamos em até 12 vezes e fazemos entrega grátis para mais informações e só chama no Whatsapp 85 9... ver número28 temos o menor preço da Região Relogios com garantia.\n\ntambém trabalhamos com bvlgari"[:100]
    produto_obtido_3.predicao='Falso'
    produto_obtido_3.percentual=75.0
    produto_obtido_3.link='https://www.facebook.com/marketplace/saopaulo/search/?callsite=commerce_mktplace_www_hoisted_pdp&hoisted_item=683536978826430&query=invicta'[:30]

    produtos_obtidos.append(produto_obtido)
    produtos_obtidos.append(produto_obtido_2)
    produtos_obtidos.append(produto_obtido_3)

    return render(request,'dashboards.html',{'table_result' : produto, 'anuncios' : produtos_obtidos})

'''def home(request):
    return render(request,'home.html',{'tela' : 'Início'})

def project(request):
    return render(request, 'project.html',{'tela' : 'O Projeto'})

def about(request):
    return render(request, 'about.html',{'tela' : 'Sobre nós'})

@login_required
def enjoy(request):
    return render(request, 'enjoy.html',{'tela' : 'Principal'})

@login_required
def search(request):
    req = request.POST.get('produto')
    if(req):
        produto = Produtos.objects.get(id_produto=req)
        marca = produto.id_marca
        anuncios = Anuncios.objects.filter(id_produto=produto)
        ia = IA()
        ia.trainning(anuncios)
        #ia.find_got_products(produto.nome)
        produtos_obtidos = []
        produto_obtido = Anuncios_obtidos()
        produto_obtido.nome='Zeus'
        produto_obtido.autor='Invicta'
        produto_obtido.preco=1000.50
        produto_obtido.descricao='Invicta Zeus'
        
        produto_obtido_2 = Anuncios_obtidos()
        produto_obtido_2.nome='Zeus réplica'
        produto_obtido_2.autor='José'
        produto_obtido_2.preco=100.50
        produto_obtido_2.descricao='Invicta aa Zeus'

        produtos_obtidos.append(produto_obtido)
        produtos_obtidos.append(produto_obtido_2)

        for produtos in produtos_obtidos:
                produtos.predict = ia.predict(produtos,marca)

        return render(request,'enjoy.html',{'tela' : 'Principal','res' : produtos_obtidos})

@login_required
def get_products(request):
    req = request.POST.get('marca')
    if (req):
        marca_ = Marcas.objects.get(id_marca = req)
        produtos = Produtos.objects.filter(id_marca=marca_)
        return render(request,'enjoy.html',{'tela' : 'Principal','produtos' : produtos})
    else:
        return enjoy(request)'''

