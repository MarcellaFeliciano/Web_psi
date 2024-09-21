from flask import Flask, session, request, render_template, url_for, redirect, make_response, flash

# o banco de dados mysql
from flask_mysqldb import MySQL

# Criptografia de senha 
from werkzeug.security import generate_password_hash, check_password_hash

# Gerenciador de login  - pip install Flask-Login
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)

# sessão
app.config['SECRET_KEY'] = 'senha'

"""
# Configurar app para trabalhar junto com flask-login
login_manager = LoginManager()
login_manager.init_app(app)

"""
# banco de dados
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'marcella123'
app.config['MYSQL_DB'] = 'db_teste'
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

conexao = MySQL(app)

"""

# Função utilizada para carregar o usuário da sessão (logado)
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
"""



@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        conn = conexao.connection.cursor()
        conn.execute ("INSERT INTO tb_usuarios(nome) VALUES(%s)", (nome,))
        conexao.connection.commit()
        
        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/listar-usuario')
def listar():
    conn = conexao.connection.cursor()
    conn.execute('SELECT * FROM tb_usuarios')
    users = conn.fetchall()
    conn.close()
    return render_template('listar.html', users = users)
