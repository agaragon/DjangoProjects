from django.shortcuts import render,redirect
from calcularConf.models import Empresa
from calcularConf.forms import InfoDasEmpresasForm
from django.core.files.storage import FileSystemStorage


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
        if form.is_valid():
            form.save()
            return redirect('verificarCadastros')
        # fs = FileSystemStorage()
        # fs.save(uploadedFile.name,uploadedFile)
        # listaDeEmpresas = Empresa.objects.order_by('nomeDaEmpresa')
        # dados = {'listaDeEmpresas':listaDeEmpresas}
        # return render(request,'verificarCadastros.html',context=dados)
    else:
        form = InfoDasEmpresasForm()
    return render(request,'atualizarCadastros.html',{'form':form})

    # return render(request,'atualizarCadastros.html',{'form':form})
    # form = InfoDasEmpresasForm()
    # if request.method == "POST":
    #     form = InfoDasEmpresasForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return verificarCadastrosView(request)
    #     else:
    #         print('Error, form invalid')
    # return render(request,'atualizarCadastros.html',{'form':form})
    