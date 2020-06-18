from django.shortcuts import render,redirect
from calcularConf.models import Empresa,DadosDasEmpresas
from calcularConf.forms import DadosDasEmpresasForm
from calcularConf.static.rotinas.calcularConf import receberRegistros
import json

# Create your views here.
def homeView(request):
    return render(request,'home.html')

def verificarCadastrosView(request):
    listaDeEmpresas = Empresa.objects.order_by('nomeDaEmpresa')
    dados = {'listaDeEmpresas':listaDeEmpresas}
    return render(request,"verificarCadastros.html",context = dados)

def atualizarCadastrosView(request):
    if request.method == "POST":
        form = DadosDasEmpresasForm(request.POST, request.FILES)
        dados={'form':form}
        if form.is_valid():
            form.save()
            listaDeRegistros = open('media/'+str(request.FILES['arquivo'])).read().lower()
            d = json.loads(listaDeRegistros)
            if 'pendências' in d.keys() and 'notas' in d.keys():
                pendencias = int(d['pendências'])
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

def registrosView(request):
    listaDeRegistros = DadosDasEmpresas.objects.all()
    dados = {'listaDeRegistros':listaDeRegistros}
    return render(request,'registros.html',context=dados)