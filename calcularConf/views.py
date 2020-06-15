from django.shortcuts import render
from calcularConf.models import Empresa
# Create your views here.

def homeView(request):
    return render(request,'home.html')

def verificarCadastrosView(request):
    listaDeEmpresas = Empresa.objects.order_by('nomeDaEmpresa')
    dados = {'listaDeEmpresas':listaDeEmpresas}
    return render(request,"verificarCadastros.html",context = dados)
    