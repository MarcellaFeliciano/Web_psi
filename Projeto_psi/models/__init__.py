from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from flask_mysqldb import MySQL
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# Configurações do banco de dados
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'marcella123'
app.config['MYSQL_DB'] = 'db_systemed'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Modelo de usuário
class User(UserMixin):
    def __init__(self, email, senha):
        self.id = None
        self.email = email
        self.senha = senha

    def get_id(self):
        return str(self.id)

    @classmethod
    def get(cls, id):
        cursor = mysql.connection.cursor()
        SLCT = 'SELECT * FROM usuarios WHERE id = %s'
        cursor.execute(SLCT, (id,))
        dados = cursor.fetchone()
        cursor.close()

        if dados:  # Corrigido para verificar dados
            user = User(email=dados['email'], senha=dados['senha'])
            user.id = dados['id']
            return user
        return None

    @classmethod
    def get_by_email(cls, email):
        cursor = mysql.connection.cursor()
        SLCT = 'SELECT * FROM usuarios WHERE email = %s'
        cursor.execute(SLCT, (email,))
        dados = cursor.fetchone()
        cursor.close()

        if dados:
            user = User(email=dados['email'], senha=dados['senha'])
            user.id = dados['id']
            return user
        return None

    def save(self):        
        cursor = mysql.connection.cursor()
        try:
            cursor.execute("INSERT INTO usuarios(email, senha) VALUES (%s, %s)", (self.email, self.senha))
            self.id = cursor.lastrowid
            mysql.connection.commit()
        except Exception as e:
            print(f"Erro ao salvar usuário: {e}")
            return False
        finally:
            cursor.close()
        return True
    
    @classmethod
    def exists(cls, email):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        if user: #melhorar esse if-else
            return True
        else:
            return False
    

# Resto do seu código, como rotas e inicialização do Flask