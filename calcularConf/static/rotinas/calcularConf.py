import math
from calcularConf.models import Empresa

def adNota(empresa):
    result = empresa.indiceDeConf*1.02
    if result > 100:
        result = 100
    empresa.indiceDeConf = math.floor(result)

def adPend(empresa):
    result = empresa.indiceDeConf - empresa.indiceDeConf*0.04
    if result < 1:
        result = 1
    empresa.indiceDeConf = math.ceil(result)

def adNotas(empresa,qtdNotas):
    for i in range(1,qtdNotas):
        adNota(empresa)

def adPends(empresa,qtdPends):
    for i in range(1,qtdPends):
        adPend(empresa)