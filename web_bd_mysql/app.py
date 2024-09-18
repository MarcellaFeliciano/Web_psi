from flask import Flask, session, request, render_template, url_for, redirect, make_response, flash

# o banco de dados mysql
from flask_mysqldb import MySQL

# Criptografia de senha 
from werkzeug.security import check_password_hash, generate_password_hash

# Gerenciador de login  - pip install Flask-Login
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)

# Configurar app para trabalhar junto com flask-login
login_manager = LoginManager()
login_manager.init_app(app)


app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'marcella123'
app.config['MYSQL_DB'] = 'db_estudos'
# retornar os dados como discionários
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# sessão
app.config['SECRET_KEY'] = 'senha'


# 4-  Função utilizada para carregar o usuário da sessão (logado)
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def index():    
    return render_template('index.html')
