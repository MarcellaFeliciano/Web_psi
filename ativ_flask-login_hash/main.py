from flask import Flask, session, request, render_template,url_for, redirect, make_response, flash
import sqlite3

from flask_login import LoginManager, login_required, login_user, logout_user
# função que faz o gerenciamento / função que bloqueia o acesso / função que diz que existe um usuario ativo / faz o logout

from models import User  # importar a classe User de Models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'muitodificil'

login_manager = LoginManager() # Faz o gerenciamento do flask-login com o app

login_manager.init_app(app) # inicializa o gerenciamento do flask-login com app

# VAI RETORNAR O USUARIO SELECIONADO
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
 #Do objeto user eu pego o usuario de acordo com o id no banco de dados - retornando os dados do usuario selecionado


#Criando uma constante com o nome do arquivo do BD.
DATABASE = 'database.db'


# obtém conexão com o banco de dados
def get_connection():
    #Colocando na variavel "conn" a conexão com o banco
    #connect(Nome do arquivo do banco), que está salvo na variavel "DATABASE" criada na linha 4.
    conn = sqlite3.connect(DATABASE)
    #comando pra transformar as tuplas (valor padrão de retorno) em dicionários.
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dash')
@login_required # se não existir usuario logado não deixa passar! / para personalizar a pagina de "erro" ver na Documentação
def dash():
    
    if 'user' not in session:
        return redirect(url_for('index'))
    
    nome = session['user']

    conexao = get_connection()
    SELECT = 'SELECT * FROM usuarios WHERE email=?'
    user = conexao.execute(SELECT,(nome,)).fetchone() # fetchone retorna uma lista
    #user = conexao.execute('SELECT * FROM usuarios WHERE email=?', (nome,)).fetchone()

    return render_template('dashboard.html', nome=user['nome'], usuario=user['usuario'], senha=user['senha']) # pega o valor (nome) salvo no bd /  nome=bancodados[usuario][1]


@app.route('/login', methods=['POST','GET'])
def login():
    if 'user' in session:
        return redirect(url_for('dash'))
    
    if request.method == 'GET':
        return render_template('login.html')
    
    else:
        email = request.form['usuario']
        senha = request.form['senha']
        #nome = request.form['nome']

        #conexao = get_connection()
       # SELECT = 'SELECT * FROM users WHERE email=?'
       # user = conexao.execute(SELECT,(email,)).fetchone()

        user = User.get_by_email(email)

        if user and user['senha'] == senha:

            login_user(user)
            session['user'] = user['nome']
            return redirect(url_for('dash'))
        
        else:
            # caso o login do usurairo não estiver cadastrado ou a senha do usurario que está cadastrado está erradpo! 
            return render_template('erro_login.html')


@app.route("/logout")
@login_required
def logout():
    
    logout_user()
    if 'user' in session:
        session.pop('user', None)
        return render_template('index.html')
    
    else:
        return 'oi'



@app.route('/cadastro', methods=['POST','GET'])
def cadastro():

      # se tentar acessar o cadastro já estando logado!
    if 'user' in session:
        return redirect(url_for('dash'))
    
    if request.method == 'GET':
        return render_template('cadastro.html')
    
    else:
        email = request.form['usuario']
        senha = request.form['senha']
        nome = request.form['nome']
        
        conexao = get_connection()
        SELECT = 'SELECT * FROM users WHERE email=?'
        user = conexao.execute(SELECT,(email,)).fetchone()

        if user:
            return 'cadastrado'
        else:
        #if nome not in bancodados:
            # se o usuario ainda não está cadastrada no dicionario/banco de dados

            #if not usuario:
                #flash('Email é obrigatório')
            #else:
                
            conexao.execute("INSERT INTO users(nome, email, senha) VALUES (?,?,?)", (nome, email, senha))
            conexao.commit()
            conexao.close()

            session['user'] = nome
            return redirect(url_for('dash'))
    
    return redirect(url_for('dash'))

# se o usuario está cadastrado significa que ele pode seguir para o dashboard
 # vai inicializar uma sessão que guardará um cookie na pagina web - saivando como ususario cadastrado igual o ultimjo usuario salvo ! o user

    

@app.route('/sobre', methods=['POST','GET'])
def sobre():
    if request.method == 'GET':

        #Pegando a variavel que faz conexão com o BD pela função get_connection (linha 13)
        conn = get_connection()

        #Usando (SELECT *) na tabela "users" do BD
        #Usando a função "fetchall" para pegar todas as colunas da tabela.
        users = conn.execute("SELECT * FROM users").fetchall()
        
        conn.close()
        return render_template('sobre.html', users=users)
    

         

"""


if 'name' in request.cookies: # se existir cookie
            if nome != request.cookies['name']: 
                # se o cookie for difenrete eu altero o nome do usuario
                # definir novo cookie
                template = redirect(url_for('dash'))
                resp = make_response(template)
                resp.delete_cookie("name") # apago o cookie antigo
                resp.set_cookie("name", value=nome)
                return resp

            else:
                # se o cookie for igual não há mudança no nome do cookie armazenado
                return redirect(url_for('dash'))
        else:
            template = redirect(url_for('dash'))
            resp = make_response(template)
            resp.set_cookie("name", value=nome)
            return resp


            usuario=request.cookies['name']
"""

