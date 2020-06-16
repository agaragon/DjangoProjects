from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from calcularConf.views import homeView,verificarCadastrosView,atualizarCadastrosView
from django.template.loader import render_to_string


# Crie seus testes aqui
class HomePageTest(TestCase):
    def testRootUrlResolvesToHomePageView(self):
        found = resolve('/')
        self.assertEqual(found.func,homeView)

    def testHomeViewReturnsCorrectHtml(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')



class VerificarCadastrosTest(TestCase):
    def testRootUrlResolvesToVerificarCadastrosView(self):
        found = resolve('/verificarCadastros/')
        self.assertEqual(found.func,verificarCadastrosView)

    def testVerificarCadastrosViewReturnsCorrectHtml(self):
        response = self.client.get('/verificarCadastros/')
        self.assertTemplateUsed(response,'verificarCadastros.html')


class AtualizarCadastrosTest(TestCase):
    def testRootUrlResolvesToAtualizarCadastrosView(self):
        found = resolve('/atualizarCadastros/')
        self.assertEqual(found.func,atualizarCadastrosView)
        
        
    def testAtualizarCadastrosViewCorrectHtml(self):
        response = self.client.get('/atualizarCadastros/')
        self.assertTemplateUsed(response,'atualizarCadastros.html')

