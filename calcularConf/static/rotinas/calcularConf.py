import math
from calcularConf.models import Empresa

def adNotas(empresa):
    id = empresa.id
    result = empresa.indiceDeConf
    for i in range(1,empresa.qtdDeNotasEmitidas):
        result*=1.02
    if result > 100:
        result = 100
    return math.floor(result)
    # empresa.indiceDeConf = math.floor(result)
    # empresa.save()

def adPends(empresa):
    id = empresa.id
    result = empresa.indiceDeConf
    for i in range(1,empresa.qtdDePendencias):
        result*=0.96
    if result < 1:
        result = 1
    return math.ceil(result)
    # empresa.indiceDeConf = math.ceil(result)
    # empresa.save()
