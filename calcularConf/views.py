from django.shortcuts import render,redirect
from calcularConf.models import Empresa,DadosDasEmpresas
from calcularConf.forms import DadosDasEmpresasForm
from calcularConf.static.rotinas.calcularConf import receberRegistros
import json
#Essa etapa é necessária para importar o módulo popularBancoDeDados
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import popularBancoDeDados


# Create your views here.
def homeView(request):
    return render(request,'home.html')


#Leva o usuário à tabela onde estão os cadastros das empresas. Caso não haja nenhum cadastro e ele clique em "Criar cadastro de empresas",
#as entradas da tabela referentes às empresas serão geradas e mostradas ao usuário.
def verificarCadastrosView(request):
    listaDeEmpresas = Empresa.objects.order_by('nomeDaEmpresa')
    dados = {'listaDeEmpresas':listaDeEmpresas}
    if request.method == 'POST':
        popularBancoDeDados.popular(50)
    return render(request,"verificarCadastros.html",context = dados)

#Se o usuário fizer o upload de um arquivo, e clicar em enviar, uma requeste com o método POST irá carregar o arquivo carregado no
#dicionário request.FILES. O arquivo será então verificado se de acordo com os critérios de validação e caso os satisfaça,
#será salvo na pasta "media". Em seguida esse arquivo será lido e seus dados utilizados para atualizar os dados de registro da empresa.

def atualizarCadastrosView(request):
    if request.method == "POST":
        form = DadosDasEmpresasForm(request.POST, request.FILES)
        dados={'form':form}
        if form.is_valid():
            form.save()
            listaDeRegistros = open('media/'+str(request.FILES['arquivo'])).read().lower()
            d = json.loads(listaDeRegistros)
            if 'pendencias' in d.keys() and 'notas' in d.keys():
                pendencias = int(d['pendencias'])
                notas = int(d['notas'])
                empresaId = request.POST['empresa']
                receberRegistros(empresaId,pendencias,notas)
                return redirect('verificarCadastros')
            else:
                form = DadosDasEmpresasForm()
                return render(request,'atualizarCadastros.html',context ={'form':form,'raiseAlert':'raiseAlert'})
    else:
        form = DadosDasEmpresasForm()
    return render(request,'atualizarCadastros.html',{'form':form})

#Busca no banco de dados os registros das empresas e os apresenta ao usuário.
def registrosView(request):
    listaDeRegistros = DadosDasEmpresas.objects.all()
    dados = {'listaDeRegistros':listaDeRegistros}
    return render(request,'registros.html',context=dados)