from flask import Flask, redirect, render_template, url_for, request, flash

import sqlite3

from models import User

# criptografia
from werkzeug.security import check_password_hash, generate_password_hash

# LoginManager
from flask_login import LoginManager, login_user, login_required, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'muitodificil'

login_manager = LoginManager() # Faz o gerenciamento do flask-login com o app

login_manager.init_app(app) # inicializa o gerenciamento do flask-login com app


# VAI RETORNAR O USUARIO SELECIONADO
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
#Do objeto user eu pego o usuario de acordo com o id no banco de dados - retornando os dados do usuario selecionado

@app.route('/')
def index():
    return render_template(index.html)

@app.route('/dash')
def dash():
    return render_template('dashboard.html')

@app.route('/cadastrar', methods=['POST','GET'])
def cadastrar():
    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']   

        if not User.exists(email):

            user = User(nome=nome, email=email, senha=senha)
            user.save() 

            # logar o usuário após cadatro
            login_user(user)

            flash("Cadastro realizado com sucesso")
            return redirect(url_for('dash'))
    else:
        return render_template('cadastrar.html')



@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['senha']  

        user = User.get_by_email(email)

        if check_password_hash(user['senha'], senha):
            #logar o usuario
            login_user(User.get(user['id']))
            flash("Você está logado")
            return redirect(url_for('dash'))
        
        else:
            flash("Dados incorretos")
            return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))