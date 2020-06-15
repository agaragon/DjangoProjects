from selenium import webdriver
from django.test import TestCase
from models import Empresa
from popularBancoDeDados import popular
from calcularConf.static.rotinas.calcularConf import adNotas,adPends

import unittest

# Crie seus testes aqui
class mudarIndiceDeConf(TestCase):
    def iniciar(self):
        self.browser = webdriver.Firefox()
    
    def terminar(self):
        self.browser.quit()
    
    def  adNotaCheck(self):
        empresa = popular(1)
        adNotas(empresa,500)
        Empresa.objects.filter(id=empresa.id).delete()


    def adPendCheck(self):
        empresa = popular(1)
        adPends(empresa,500)
        Empresa.objects.filter(id=empresa.id).delete()

if __name__ == '__main__':
    unittest.main(warnings='ignore')