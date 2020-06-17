from django.shortcuts import render,redirect
from calcularConf.models import Empresa,InfoDasEmpresas
from calcularConf.forms import InfoDasEmpresasForm
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
        form = InfoDasEmpresasForm(request.POST, request.FILES)
        dados={'form':form}
        if form.is_valid():
            form.save()
            listaDeRegistros = open('media/'+str(request.FILES['arquivo'])).read()
            d = json.loads(listaDeRegistros)
            pendencias = int(d['Pendencias'])
            notas = int(d['Notas'])
            empresaId = request.POST['empresa']
            receberRegistros(empresaId,pendencias,notas)
            return redirect('verificarCadastros')
    else:
        form = InfoDasEmpresasForm()
    return render(request,'atualizarCadastros.html',{'form':form})

def registrosView(request):
    listaDeRegistros = InfoDasEmpresas.objects.all()
    dados = {'listaDeRegistros':listaDeRegistros}
    return render(request,'registros.html',context=dados)