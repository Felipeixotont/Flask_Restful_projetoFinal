<h3 align="center"> Criando nosso Banco de Dados. </h3>
<hr>

Primeiro criamos a estrutura do nosso Banco de Dados utilizando SQLAlchemy.

<p>Nosso banco terá as tabelas:</p>
<ul>
  <li>Usuarios -> (Possuindo as colunas Login e Senha);
  <li>Pessoas -> (Possuindo as colunas ID, Nome e idade).  
</ul>

<h6 align="center">Arquivo Models</h6>

![carbon (1)](https://user-images.githubusercontent.com/43455579/134454567-24a4f640-8db7-4868-8f79-de0d37c66824.png)

<h3 align="center"> Criando as tabelas e inserindo informações para teste. </h3>
<hr>
<h6 align="center">Arquivo Utils</h6>

![carbon](https://user-images.githubusercontent.com/43455579/134454520-1e50e582-9167-4fee-ad6a-c6dfdafe2647.png)

<h3 align="center"> Conferindo os dados atuais da nossa tabela. </h3>
<hr>

Obs.: Houve uma tentativa de acessar o banco usando um login inexistente para realizar o teste. Como mostra a imagem o acesso não foi autorizado, 
então em seguida é informado um login e senha válidos no sistema, exibindo toda nossa tabela.

![Postman 2021-09-22 23-39-01](https://user-images.githubusercontent.com/43455579/134450843-1605e351-7934-4bc3-9cbb-afdacad88869.gif)

