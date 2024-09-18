from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

database = 'database.db'

def get_connection():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn


# classe que recebe as informações do usuario
class User(UserMixin):
    _hash : str
    def __init__(self, **kwargs):
        self._id = None
        if 'nome' in kwargs.keys():
            self._nome = kwargs['nome']
        if 'email' in kwargs.keys():
            self._email = kwargs['email']
        if 'senha' in kwargs.keys():
            self._password = kwargs['senha']
        if 'hash' in kwargs.keys():
            self._hash = kwargs['hash']
      
       
    # sobresrever get id do UserMixin
    def get_id(self):
        return str(self._id)

    
    # usada para definir senha como uma propriedade
    @property
    def _password(self):
        return self._hash
    
    # limita o acesso a senha para atribuição de valor
    # sempre salva o hash a partir da senha
    @_password.setter
    def _password(self, senha):
        self._hash = generate_password_hash(senha)
    
    # ----------métodos para manipular o banco--------------#
    def save(self):        
        conn = get_connection()  
        cursor = conn.cursor()      
        cursor.execute("INSERT INTO tb_users(nome, email, senha) VALUES (?,?,?)", (self._senha, self._email, self._hash))
        # salva o id no objeto recem salvo no banco
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()
        return True
 

# selecionar o usuario pelo id 
    @classmethod
    def get(cls,user_id):
        conn = get_connection()
        user = conn.execute("SELECT * FROM tb_users WHERE id = ?", (user_id,)).fetchone()
        conn.close()
        if user:
            loaduser = User(email=user['email'] , hash=user['senha'])
            loaduser._id = user['id']
            return loaduser
        else:
            return None
    
    @classmethod
    def exists(cls, email):
        conn = get_connection()
        user = conn.execute("SELECT * FROM tb_users WHERE email = ?", (email,)).fetchone()
        conn.close()
        if user: 
            return True
        else:
            return False
    
    @classmethod
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT id, email FROM tb_users").fetchall()
        conn.close()
        return users
    
       
    @classmethod
    def get_by_email(cls,email):
        conn = get_connection()
        user = conn.execute("SELECT id, nome, email, senha FROM tb_users WHERE email = ?", (email,)).fetchone()
        conn.close()
        return user