<h3 align="center"> Criando nosso Banco de Dados. </h3>
<hr>

Primeiro criamos a estrutura do nosso Banco de Dados utilizando SQLAlchemy.

<p>Nosso banco terá as tabelas:</p>
<ul>
  <li>Usuarios -> (Possuindo as colunas Login e Senha);
  <li>Pessoas -> (Possuindo as colunas ID, Nome e idade).  
</ul>

<h6 align="center">Arquivo Models</h6>

![models](https://user-images.githubusercontent.com/43455579/134429097-35c6223d-9e33-4874-a103-c29a98c84e55.png)

<h3 align="center"> Criando as tabelas e inserindo informações para teste. </h3>
<hr>
<h6 align="center">Arquivo Utils</h6>

![utils](https://user-images.githubusercontent.com/43455579/134429806-cb9ad488-7717-45ea-a574-0fd3cf9ec5a6.png)

<h3 align="center"> Conferindo os dados atuais da nossa tabela. </h3>
<hr>

Obs.: Houve uma tentativa de acessar o banco usando um login inexistente para realizar o teste. Como mostra a imagem o acesso não foi autorizado, 
então em seguida é informado um login e senha válidos no sistema, exibindo toda nossa tabela.

![Postman 2021-09-22 23-39-01](https://user-images.githubusercontent.com/43455579/134450843-1605e351-7934-4bc3-9cbb-afdacad88869.gif)

