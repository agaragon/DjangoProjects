import math
from calcularConf.models import Empresa

def adNotas(empresa):
    result = empresa.indiceDeConf
    for i in range(1,empresa.qtdDeNotasEmitidas):
        result*=1.02
    if result > 100:
        result = 100
    empresa.indiceDeConf = math.floor(result)

def adPends(empresa):
    result = empresa.indiceDeConf
    for i in range(1,empresa.qtdDePendencias):
        result*=0.96
    if result < 1:
        result = 1
    empresa.indiceDeConf = math.ceil(result)

