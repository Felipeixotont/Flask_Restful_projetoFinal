from models import Pessoas, Usuarios


#  insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Felipe', idade=28)
    print(pessoa)
    pessoa.save()


#  exibe todas as pessoas da tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)


#  altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.nome = 'Brenda'
    pessoa.idade = 28
    pessoa.save()


#  exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()


#  insere usuario na tabela usuario
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


# exibe todos os usuarios da tabela
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    #  insere_usuario('felipeixotont', '1234')
    #  insere_usuario('arthuroliv', '4321')
    #  insere_pessoas()
    #  altera_pessoa()
    #  exclui_pessoa()
    consulta_todos_usuarios()
    consulta_pessoas()
