
# arquivo de classes que serão utilizados no projeto

from flask_login import UserMixin

import sqlite3

def get_connection():
    #Colocando na variavel "conn" a conexão com o banco
    #connect(Nome do arquivo do banco), que está salvo na variavel "DATABASE" criada na linha 4.
    conn = sqlite3.connect('database.db')
    #comando pra transformar as tuplas (valor padrão de retorno) em dicionários.
    conn.row_factory = sqlite3.Row
    return conn


class User(UserMixin): 
    id : str    # ele obrigatoriamente tem que ser string
    def __init__(self,nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha



    @classmethod   # metodo que se refere a classe
    def get(cls, id):
        conn = get_connection()
        SELECT = 'SELECT * FROM users WHERE id=?'
        dados = conn.execute(SELECT,(id,)).fetchone()
        user = User(dados['nome'], dados['email', dados['senha']])  # esse usuario vai ser representado na classe User!
        user.id = dados['id']
        return user 



    @classmethod   # metodo que se refere a classe
    def get_by_email(cls, email):
        conn = get_connection()
        SELECT = 'SELECT * FROM users WHERE email=?'
        dados = conn.execute(SELECT,(email,)).fetchone()
        if dados:
            user = User(dados['nome'], dados['email'], dados['senha'])  # esse usuario vai ser representado na classe User!
            user.id = dados['id']
            return user 
        else:
            return None # se não exixtir usuario cadastrado não irá logar, logo o resutado é None
