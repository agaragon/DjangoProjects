import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','confEmpresas.settings')
import django
django.setup()
import random
import uuid 
from calcularConf.models import Empresa
from faker import Faker

django.setup()

fakegen = Faker()

def popular(N=5):

    for entry in range(N):
        empresa = fakegen.company()
        id = uuid.uuid1()
        qtdDeNotas = random.randint(0,200)
        qtdDePendencias = random.randint(0,200)
        indiceDeConfFloat = random.randint(1,100)
        indiceDeConfInt = random.randint(1,100)
        return Empresa.objects.get_or_create(nomeDaEmpresa = empresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,idDaEmpresa = id,indiceDeConfInt = indiceDeConfInt,indiceDeConfFloat=indiceDeConfInt)[0]
        

if __name__ == '__main__':
    print('Populando banco de dados')
    popular(50)
    print('Processo completo')
