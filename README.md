# README #

### Objetivo do repositório ###

* O objetivo desse repositório é disponibilizar uma aplicação django para o desafio proposto pela Serasa. Aqui você encontra um passo a passo de como 
fazer o setup da aplicação. A aplicação está disponível em: https://andregaragon@bitbucket.org/andregaragon/confempresas.git e seu download pode ser 
feito através do comando "git clone https://andregaragon@bitbucket.org/andregaragon/confempresas.git", sem áspas.

### Como fazer o setup ###

* Após o download do repositório, abra o prompt de comando na pasta do projeto. Nessa pasta você precisará dos arquivos requirements.txt, manage.py e
popularBancoDeDados.py. Certifique-se de que eles se encontram no seu diretório atual.
Summary of set up
* crie um virtual environment, o comando "virtualenv myEnv" pode ser utilizado, caso o pacote virtualenv tenha sido instalado.
* Ative o seu virtual environment.
* As dependências do projeto encontram-se no arquivo requirements.txt. Para instalá-las, utilize o comando "pip install -r requirements.txt".
* Para criar o banco de dados, digite os seguintes comandos no seu prompt de comando:
- python manage.py makemigrations
- python manage.py migrate
* Para popular o banco de dados com as empresas cadastradas, foi criado o arquivo "popularBancoDeDados.py". Ative-o com o comando "python popularBancoDeDados.py".
* Na pasta dummyFiles há um gerador de arquivos com dados de registro das empresas, assim como diversos registros. Para criar novos registros digite no prompt de comando:

- cd dummyFiles
- python createDummyFiles.py
- cd ..

* Alternativamente, você pode criar um registro. Os registros estão no formato .json e devem terminar com .json. Seu conteúdo deve seguir o seguinte padrão: {"pendencias":"<Número de pendências>","notas":"<Número de notas emitidas>"}, por exemplo: {"pendencias":"5","notas":"2"}. Observação: não ponha acento circunflexo em "pendências".
* Agora digite "python manage.py runserver" no prompt de comando, a sua aplicação deve estar rodando agora no seu servidor local.
* Um link para o acesso à aplicação será apresentado no seu prompt de comando, geralmente http://localhost:8000/. Copie-o e cole-o na barra de endereços do seu browser para acessar a aplicação.
* How to run tests

### Descrição do código ###

* A plataforma foi criada utilizando o framework django, que faz uso da linguagem python para prover ferramentas para gerar e gerenciar uma plataforma web. 
* Dentro do projeto são encontrados inicialmente 4 pastas: calcularConf,confEmpresas,dummyFiles e staticfiles. Além disso uma quinta pasta, chamada "media" será criada quando o usuário fizer o upload de um arquivo.
* A pasta calcularConf é responsável por gerenciar a interface (arquivo views.py e subpasta static), configurações do banco de dados (arquivo models.py),assim como acesso e registro ao mesmo (views.py), e tratamento de dados recebidos pelo servidor para o cálculo dos índice de confiabilidade. Além disso, podem ser encontrados testes unitários, referentes ao fluxo de dados dentro da aplicação, e testes funcionais, referentes à experiência do usuário interagindo com a plataforma.
* A pasta confEmpresas é responsável pelo gerenciamento da plataforma como um todo. Criação do banco de dados, direcionamento de urls, entre outros.
* A pasta dummyFiles foi criada para armazenar os arquivos com os registros das empresas antes do upload.
* a pasta que será posteriormente criada, "media", irá armazenar os dados de empresas cujo upload foi feito, para posterior acesso pelo usuário.

* A rotina para o cálculo do índice de confiabilidade pode ser encontrada no diretório calcularconf/static/rotinas/calcularConf.py, assim como a sua respectiva documentação.
* As rotinas para a validação dos dados do usuário podem ser encontradas em calcularconf/static/rotinas/validators.py. As duas validações contidas nesse arquivo dizem respeito ao tamanho do arquivo e ao formato. O tamanho não deve exceder 2kb e o final do arquivo deve ser .json, para informar o usuário que o arquivo deve estar no formato .json, porém, caso a sua organização interna não seja no formato json, uma rotina em views.py irá gerar um alerta ao usuário, instruindo-o a respeito da correta maneira de entrar com os dados.
* Os testes utilizados se encontram no arquivo tests.py e functional_tests.py, dentro da pasta "calcularConf" e são dividos entre testes funcionais, os quais simulam a interação do usuário com a interface, e testes unitários, os quais simulam as a atividade do backend perante as interações do usuário. 
* Para rodar os testes unitários, basta utilizar o comando "python manage.py test", a partir da pasta da pasta calcularConf. As descrições do funcionamento dos testes estão dentro do arquivo tests.py.
* Para rodar os testes funcionais, utilize o comando python functional_tests.py. As descrições do funcionamento do teste estão dentro do arquivo functional_tests.py.

### Banco de dados ###

* O banco de dados possue duas tabelas: uma para os dados das empresas, e outra para os dados das empresas.
* A tabela para as empresas possui os campos nomeDaEmpresa, qtdDeNotasEmitidas, qtdDePendencias e indiceDeConf, além de uma Id gerada automaticamente pela plataforma django. Essa id será utilizada para associar as empresas aos seus registros.
* A tabela para os dados das empresas possui uma entrada para um endereço de diretório de arquivo, no qual o arquivo carregado para plataforma foi armazenado, uma campo para armazenar o mês do registro e um campo de chave estrangeira para conectar cada registro a uma empresa. Dessa maneira, uma empresa pode possuir diversos registros, porém cada registro pertence a apenas uma empresa.

### Utilização da plataforma ###

* Acesse a plataforma através do link http://localhost:8000/, o qual o direcionará para a homepage. Caso não consiga acessar a plataforma, leia novamente a as instruções em "Como fazer o setup";
* Há 4 urls que podem ser usadas: "/", "/verificarCadastros/", "/atualizarCadastros/" e "/registros/". As 4 urls podem ser acessadas através da navbar.
* A url "/" leva o usuário à homepage e possui um resumo do objetivo da aplicação, além de explicar como o cálculo do índice de confiabilidade é efetuado.
* A url "/verificarCadastros/" leva o usuário para a tabela onde ele pode encontrar diversas empresas assim como os seus respectivos índices de confiabilidade. Caso não haja nenhuma empresa listada, uma mensagem é apresentada ao usuário informando-o do mesmo, juntamente com um botão com a opção de popular o banco de dados com empresas fictícias.
* A url "/atualizarCadastros/" leva o usuário a uma página onde ele pode fazer o upload de arquivos no formato .json, o qual deverá conter o número de pendências e o número de notas fiscais de um determinado mês. Uma vez carregado para a nuvem, o arquivo é lido, o número de pendências e de notas é adicionado ao número de pendências e notas atual, e o índice de confiabilidade para a empresa correspondente é recalculado. Os arquivos .json devem ter o seguinte formato: {"pendencias":"<Número de pendências>","notas":"<Número de notas emitidas>"}, por exemplo: {"pendencias":"5","notas":"2"}. Observação: não ponha acento circunflexo em "pendências".
* A url "/registros/" contém os registros relacionados a cada empresa. Depois que o usuário fizer o upload do registro de uma empresa, o registro estará disponível para visualização na página registros, juntamente com o id da empresa e o mês do registro.

### Contato ###

* Meu nome: André Guimarães Aragon
* E-mail: andregaragon@gmail.com
* Telefone: (48) 9 88185545
* Página pessoal na web: www.andreguimaraesaragon.cf
# DjangoProjects
