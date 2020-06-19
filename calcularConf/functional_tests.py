from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time
class NovoVisitanteTeste(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    #Quando o usuário clica na dropdown box, ele pode ver os demais links disponíveis
    def testFuncionamentoDaNavbar(self):
        self.browser.get('http://localhost:8000')
        dropdownBox = self.browser.find_element_by_id('dropdownBox')
        ActionChains(self.browser).click(dropdownBox).perform()
        classes = dropdownBox.get_attribute('class')
        fail = True
        for aClass in classes.split(" "):
            if aClass == "show":
                fail = False
        if fail == True:
            self.fail("O dropbox não está funcionando")
    
    #Quando o usuário clica no link para acessar o cadastro das empresas, ele pode ver uma tabela cujo cabeçalho contém os tags "Nome da empresa", "Indice de confiabilidade", "Quantidades de Notas Fiscais" e "Quantidade de pendências"
    def testPodeAcessarListaDeEmpresas(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Cadastro de confiabilidade',self.browser.title)
        dropdownBox = self.browser.find_element_by_id('dropdownBox')
        ActionChains(self.browser).click(dropdownBox).perform()
        acessoParaLista = self.browser.find_element_by_link_text('Verificar cadastros')
        ActionChains(self.browser).click(acessoParaLista).perform()
        time.sleep(1)
        self.browser.find_element_by_id('cadastroDeEmpresas')

        
    #Quando o usuário clica no botão para criar o banco de dados, ele verá a tabela de registros cerca de 15 segundos depois.
    #caso o botão não seja encontrado, é porque o banco de dados não está vazio.
    def testFuncionamentoDoBotaoPopularBanco(self):
        self.browser.get('http://localhost:8000/verificarCadastros')
        try:
            popular = self.browser.find_element_by_tag_name('button')
        except:
            return
        ActionChains(self.browser).click(popular).perform()
        time.sleep(15)        
        self.browser.find_elements_by_id('tabelaDeRegistros')
        
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')