# from selenium import webdriver
from models import Empresa
from static.rotinas.calcularConf import adPend,adNota

import uuid 

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'Cadastro de confiabilidade' in browser.title

ent1 = Empresa(nomeDaEmpresa = 'test1',qtdDeNotasEmitidas = 150,qtdDePendencias = 150,idDaEmpresa = uuid.uuid1(),indiceDeConf = 50)
adNota(ent1)
if ent1.indiceDeConf == 51:
    console.log('Teste bem sucedido')
