from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from calcularConf.views import homeView,verificarCadastrosView,atualizarCadastrosView,registrosView
from calcularConf.models import Empresa,DadosDasEmpresas
import json
from calcularConf.static.rotinas.calcularConf import receberRegistros

#Testes referentes à homepage
class HomePageTest(TestCase):
    #verifica se resolvendo a rul "\", a view que é chamada corresponde à homeView
    def testRootUrlResolvesToHomePageView(self):
        found = resolve('/')
        self.assertEqual(found.func,homeView)
    
#testes referentes à página verificarCadastros
class VerificarCadastrosTest(TestCase):
    def testRootUrlResolvesToVerificarCadastrosView(self):
        found = resolve('/verificarCadastros/')
        self.assertEqual(found.func,verificarCadastrosView)

    def testVerificarCadastrosViewReturnsCorrectHtml(self):
        response = self.client.get('/verificarCadastros/')
        self.assertTemplateUsed(response,'verificarCadastros.html')

#testes referentes à página atualizarCadastros
class AtualizarCadastrosTest(TestCase):
    def testRootUrlResolvesToAtualizarCadastrosView(self):
        found = resolve('/atualizarCadastros/')
        self.assertEqual(found.func,atualizarCadastrosView)
        
    def testAtualizarCadastrosViewCorrectHtml(self):
        response = self.client.get('/atualizarCadastros/')
        self.assertTemplateUsed(response,'atualizarCadastros.html')

    def testBancoDeDadosSalvaEDeletaCorretamente(self):
        nomeDaEmpresa = 'teste'
        qtdDeNotas = 0
        qtdDePendencias = 0
        indiceDeConf = 50
        inicial = Empresa.objects.all().count()
        empresa = Empresa.objects.create(nomeDaEmpresa = nomeDaEmpresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,indiceDeConf = indiceDeConf)
        final = Empresa.objects.all().count()
        self.assertEqual(inicial+1,final) 
        empresa.delete()
        final = Empresa.objects.all().count()
        self.assertEqual(inicial,final) 

        #verifica se o valor retornado pela função "receber registros" é compatível com os valores esperados. Note que o menor índice que uma empresa
        #pode atingir é 24, valores inferiores a esse não são alcançados.
    def testCalculoDoIndiceDeConfiabilidade(self):
        nomeDaEmpresa = 'teste'
        qtdDeNotas = 0
        qtdDePendencias = 0
        indiceDeConf = 50
        empresa = Empresa.objects.create(nomeDaEmpresa = nomeDaEmpresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,indiceDeConf = indiceDeConf)
        self.assertEqual(receberRegistros(empresa.id,qtdDePendenciasDetectadas=1,qtdDeNotasRecebidas=3),51)
        empresa = Empresa.objects.create(nomeDaEmpresa = nomeDaEmpresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,indiceDeConf = indiceDeConf)
        self.assertEqual(receberRegistros(empresa.id,qtdDePendenciasDetectadas=10,qtdDeNotasRecebidas=4),41)
        empresa = Empresa.objects.create(nomeDaEmpresa = nomeDaEmpresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,indiceDeConf = indiceDeConf)
        self.assertEqual(receberRegistros(empresa.id,qtdDePendenciasDetectadas=0,qtdDeNotasRecebidas=50),100)
        empresa = Empresa.objects.create(nomeDaEmpresa = nomeDaEmpresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,indiceDeConf = indiceDeConf)
        self.assertEqual(receberRegistros(empresa.id,qtdDePendenciasDetectadas=0,qtdDeNotasRecebidas=51),100)
        empresa = Empresa.objects.create(nomeDaEmpresa = nomeDaEmpresa,qtdDeNotasEmitidas = qtdDeNotas,qtdDePendencias = qtdDePendencias,indiceDeConf = indiceDeConf)
        self.assertEqual(receberRegistros(empresa.id,qtdDePendenciasDetectadas=1000,qtdDeNotasRecebidas=0),24)
        
        

#testes referentes à página registros1
class RegistrosTest(TestCase):
    def testRootUrlResolvesToAtualizarCadastrosView(self):
        found = resolve('/registros/')
        self.assertEqual(found.func,registrosView)
        
        
        
    def testAtualizarCadastrosViewCorrectHtml(self):
        response = self.client.get('/registros/')
        self.assertTemplateUsed(response,'registros.html')

    
