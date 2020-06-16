from django.urls import resolve
from django.test import TestCase
from calcularConf.views import homeView,verificarCadastrosView,atualizarCadastrosView

# Crie seus testes aqui
class HomePageTest(TestCase):
    def testRootUrlResolvesToHomePageView(self):
        found = resolve('/')
        self.assertEqual(found.func,homeView)

class VerificarCadastrosTest(TestCase):
    def testRootUrlResolvesToVerificarCadastrosView(self):
        found = resolve('/verificarCadastros/')
        self.assertEqual(found.func,verificarCadastrosView)

class AtualizarCadastrosTest(TestCase):
    def testRootUrlResolvesToAtualizarCadastrosView(self):
        found = resolve('/atualizarCadastros/')
        self.assertEqual(found.func,atualizarCadastrosView)

