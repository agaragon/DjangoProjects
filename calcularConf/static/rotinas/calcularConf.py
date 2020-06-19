import math
from calcularConf.models import Empresa

def adNotas(empresaId,qtdDeNotasRecebidas):
    empresa = Empresa.objects.filter(id=empresaId)[0]
    empresa.qtdDeNotasEmitidas = qtdDeNotasRecebidas
    empresa.save()
    result = empresa.indiceDeConf
    for i in range(0,empresa.qtdDeNotasEmitidas):
        result=math.floor(1.02*result)
    if result > 100:
        result = 100
    return math.floor(result)

def adPends(empresaId,qtdDePendenciasDetectadas):
    empresa = Empresa.objects.filter(id=empresaId)[0]
    empresa.qtdDePendencias = qtdDePendenciasDetectadas
    empresa.save()
    result = empresa.indiceDeConf
    for i in range(0,empresa.qtdDePendencias):
        result=math.ceil(0.96*result)
    if result < 1:
        result = 1
    return math.ceil(result)

def receberRegistros(empresaId,qtdDePendenciasDetectadas,qtdDeNotasRecebidas):
    empresa = Empresa.objects.filter(id=empresaId)[0]
    empresa.indiceDeConf = 50
    empresa.save()
    empresa.qtdDeNotasEmitidas += qtdDeNotasRecebidas
    empresa.save()
    empresa.indiceDeConf = adNotas(empresaId,empresa.qtdDeNotasEmitidas)
    empresa.save()
    empresa.qtdDePendencias += qtdDePendenciasDetectadas
    empresa.save()
    empresa.indiceDeConf = adPends(empresaId,empresa.qtdDePendencias)
    empresa.save()
    return empresa.indiceDeConf