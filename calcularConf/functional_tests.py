from selenium import webdriver
import unittest

class NovoVisitanteTeste(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def testPodeAcessarListaDeEmpresas(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Cadastro de confiabilidade',self.browser.title)
        self.fail('Terminar o teste')

if __name__ == '__main__':
    unittest.main(warnings='ignore')