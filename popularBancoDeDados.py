import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','confEmpresas.settings')
import django
django.setup()

import random
from calcularConf.models import Empresa
from calcularConf.static.rotinas.calcularConf import adNotas,adPends
from faker import Faker

fakegen = Faker()

def popular(N=5):

    for entry in range(N):
        nomeDaEmpresa = fakegen.company()
        qtdDeNotas = 0
        qtdDePendencias = 0
        indiceDeConf = 50
        empresa = Empresa.objects.get_or_create(nomeDaEmpresa = nomeDaEmpresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,indiceDeConf = indiceDeConf)[0]
        
# def popular(N=5):

#     for entry in range(N):
#         nomeDaEmpresa = fakegen.company()
#         qtdDeNotas = random.randint(0,200)
#         qtdDePendencias = random.randint(0,50)
#         indiceDeConf = 50
#         empresa = Empresa.objects.get_or_create(nomeDaEmpresa = nomeDaEmpresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,indiceDeConf = indiceDeConf)[0]
#         empresa.indiceDeConf = adNotas(empresa)
#         empresa.save()
#         empresa.indiceDeConf = adPends(empresa)
#         empresa.save()

if __name__ == '__main__':
    print('Populando banco de dados')
    popular(50)
    print('Processo completo')
