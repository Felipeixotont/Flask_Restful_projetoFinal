from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Usuarios
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

'''# dicionário com usuários e senhas que serão utilizados na autenticação.
USUARIOS = {
    'felipe': '123',
    'peixoto': '321'
}'''


'''# metodo de autenticação do usuário. Preciso colocar essa verificação em todos os metodos que quero autenticar.
@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return USUARIOS.get(login) == senha'''


@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()  # se deixarmos sem o first sempre dará True.


class Pessoa(Resource):
    @auth.login_required  # esse decorador diz que para acessar esse metodo é obrigado estar logado.
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {'status': 'error', 'mensagem': 'Pessoa nao encontrada!'}
        return response

    @auth.login_required
    def post(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json

        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        if 'id' in dados:
            pessoa.id = dados['id']

        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    @auth.login_required
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        mensagem = 'Pessoa {} excluida com sucesso!'.format(pessoa.nome)
        return {'status': 'sucesso!', 'mensagem': mensagem}


class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'nome': i.nome, 'id': i.id, 'idade': i.idade} for i in pessoas]  # for in line
        return response

    @auth.login_required
    def put(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/tabela/')

if __name__ == '__main__':
    app.run(debug=True)
