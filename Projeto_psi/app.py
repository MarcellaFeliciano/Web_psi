from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user
from models import User 
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
@app.route('/marcar_consulta', methods=['GET', 'POST'])
def marcar_consulta():
    if request.method == 'GET':   
        return render_template('marcar_consulta.html')
    
    else:
        nome = request.form['nome']
        data = request.form['data']
        horario = request.form['horario']
        email = request.form['email']
        motivo = request.form['motivo_consulta']

        cursor = mysql.connection.cursor()
        try:
            cursor.execute("INSERT INTO consultas(nome, dia, horario, email, motivo) VALUES (%s, %s, %s, %s, %s)", (nome, data, horario, email, motivo))
            mysql.connection.commit()
        except Exception as e:
            print(f"Erro ao agendar consulta: {e}")
            return render_template('marcar_consulta.html')
        
        finally:
            cursor.close()
        return render_template('index.html')


# Relatório sobre o paciente
@login_required
@app.route('/ficha', methods=['GET', 'POST'])
def ficha():
    if request.method == 'GET':   
        return render_template('ficha_paciente.html')
    else:
        nome = request.form['nome']
        data_nasc = request.form['data_nascimento']
        genero = request.form['genero']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        email = request.form['email']
        motivo = request.form['motivo_consulta']
        data_consulta = request.form['data_da_consulta']
        historico = request.form['historico_medico']
        medicamentos = request.form['medicamentos_em_uso']

        cursor = mysql.connection.cursor()
      
        try:
            cursor.execute("INSERT INTO ficha_paciente(nome, data_nasc, genero, endereco, telefone, email, motivo, data_consulta, historico, medicamentos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, data_nasc, genero, endereco, telefone, email, motivo, data_consulta, historico, medicamentos))
            mysql.connection.commit()
            flash('Ficha do paciente cadastrada com sucesso!')
        except Exception as e:
            print(f"Erro ao cadastrar ficha de paciente: {e}")
            flash('Erro ao cadastrar ficha de paciente. Verifique os dados e tente novamente.')
            return render_template('ficha_paciente.html')
        finally:
            cursor.close()
        return redirect(url_for('index')) 
        

# Ver as consultas que foram agendadas
@login_required
@app.route('/agendadas')
def agendadas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM consultas")
    consultas = cursor.fetchall()
    cursor.close()
    if consultas:
        return render_template('agendadas.html', consultas=consultas)
    return "Não existem consultas agendadas "



@login_required
@app.route('/ver_ficha', methods=['GET', 'POST'])
def ver_ficha():
    if request.method == 'GET':
        return render_template('ver_ficha.html', ficha=None)

    else:
        nome = request.form['nome']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM ficha_paciente WHERE nome = %s", (nome,))
        ficha = cursor.fetchone()  # Use fetchone() para obter um único registro
        cursor.close()

        if ficha:
            return render_template('ver_ficha.html', ficha=ficha)
        return render_template('ver_ficha.html', ficha=None, mensagem="Esta ficha não existe.")




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
def logout():
    logout_user()
    return redirect(url_for('index'))
