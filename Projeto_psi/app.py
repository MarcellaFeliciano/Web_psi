from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user
from models import User  # Certifique-se de que este módulo está correto
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL


from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VASCODAGAMA'

# Configurações do MySQL
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'marcella123'
app.config['MYSQL_DB'] = 'db_systemed'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


app.config['MAIL_SERVER'] = os.getenv('SERVER')
app.config['MAIL_PORT'] = int(os.getenv('PORT'))  # Converta para int
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('USERNAME')  # E-mail padrão

mail = Mail(app)

# Inicializa o LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

# Agendar consultas
@login_required
@app.route('/marcar_consulta')
@login_required
def marcar_consulta():
    return render_template('marcar_consulta.html')

# Relatório sobre o paciente
@login_required
@app.route('/ficha')
@login_required
def ficha():
    return render_template('ficha_paciente.html')

# Ver as consultas que foram agendadas
@login_required
@app.route('/agendadas')
@login_required
def agendadas():
    return render_template('agendadas.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html')
    
    email = request.form['email']
    senha = request.form['senha']
    senha_hash = generate_password_hash(senha)

    if not User.exists(email):
        user = User(email, senha_hash)
        try:
            user.save()  # Salva o usuário no banco de dados
            # Cria e envia o e-mail
            msg = Message("CADASTRO", recipients=[email])
            msg.body = "Você se cadastrou no SysteMed!"
            mail.send(msg)  # Envia o e-mail
            login_user(user)
            return redirect(url_for('index'))  # Redireciona para a página inicial
        except Exception as e:
            flash('email inválido')
            return render_template('cadastro.html')
    else:
        flash('Usuário já existe.')
        return redirect(url_for('cadastro'))
    


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        senha = request.form['senha']
        user = User.get_by_email(email)

        if user and check_password_hash(user.senha, senha):  # Corrigido para usar .senha
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Dados incorretos.')
            return render_template('login.html')

@login_required
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
# 