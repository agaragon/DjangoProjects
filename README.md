# README #


### Objetivo do repositório: ###

* O objetivo desse repositório é disponibilizar uma aplicação django para o desafio proposto pela Serasa. Aqui você encontra um passo a passo de como 
fazer o setup da aplicação. A aplicação está disponível em: https://andregaragon@bitbucket.org/andregaragon/confempresas.git e seu download pode ser 
feito através do comando "git clone https://andregaragon@bitbucket.org/andregaragon/confempresas.git", sem áspas.

### Como fazer o setup: ###

* Após o download do repositório, abra o prompt de comando na pasta do projeto. Nessa pasta você precisará dos arquivos requirements.txt, manage.py e
popularBancoDeDados.py. Certifique-se de que eles se encontram no seu diretório atual.
Summary of set up
* crie um virtual environment, você pode utilizar o comando "virtualenv myEnv", caso tenha virtualenv instalado.
* Ative o seu virtual environment.
* As dependências do projeto encontram-se no arquivo requirements.txt. Para instalá-las, utilize o comando "pip install -r requirements.txt".
* Para criar o banco de dados, digite os seguintes comandos no seu prompt de comando:
- python manage.py makemigrations
- python manage.py migrate
* Para popular o banco de dados com as empresas cadastradas, foi criado o arquivo "popularBancoDeDados.py". Ative-o com o comando "python popularBancoDeDados.py.
* Na pasta dummyFiles há um gerador de arquivos com dados de registro das empresas, assim como um gerador de dados de registro aleatórios. Para criar novos registros digite no prompt de comando:

- cd dummyFiles
- python createDummyFiles.py
- cd ..

* Agora digite "python manage.py runserver" no prompt de comando, a sua aplicação deve estar rodando agora no seu servidor local.
* Um link para o acesso à aplicação será apresentado no seu prompt de comando, geralmente http://localhost:8000/. Copie-o e cole-o na barra de endereços do seu browser para acessar a aplicação.
* How to run tests
* Deployment instructions

### Descrição do código ###

### Utilização da plataforma ###

* Acesse a plataforma através do link http://localhost:8000/, o qual o direcionará para a homepage. 
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact