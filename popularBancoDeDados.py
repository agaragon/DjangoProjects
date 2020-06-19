import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','confEmpresas.settings')
import django
django.setup()

from calcularConf.models import Empresa

#O pacote faker permite que sejam gerados dados fictícios para empresas
from faker import Faker
fakegen = Faker()


def popular(N=5):

    for entry in range(N):
        nomeDaEmpresa = fakegen.company()
        qtdDeNotas = 0
        qtdDePendencias = 0
        indiceDeConf = 50
        empresa = Empresa.objects.get_or_create(nomeDaEmpresa = nomeDaEmpresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,indiceDeConf = indiceDeConf)[0]
        
if __name__ == '__main__':
    print('Populando banco de dados')
    popular(50)
    print('Processo completo')
