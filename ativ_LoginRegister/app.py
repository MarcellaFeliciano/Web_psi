from flask import Flask, session, request, render_template, url_for, redirect
import sqlite3

banco_dados = 'database.db'

app = Flask(__name__)

#bancodados = {}

# chave para critografia de cookies na sessão
app.config['SECRET_KEY'] = 'superdificil'


def obter_conexao():
    conn = sqlite3.connect(banco_dados)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    if 'user' not in session:
        return redirect(url_for('index'))
    
    return render_template('dashboard.html', nome=session['user'])

@app.route('/login', methods=['POST', 'GET'])
def login():
    # se já tá logado
    if 'user' in session:
        return redirect(url_for('dash')) #vai pra o dashboard

    if request.method == 'GET':
        return render_template('login.html')
    else:
        nome = request.form['nome']
        senha = request.form['senha']

        conexao = obter_conexao()
        SELECT = 'SELECT * FROM usuarios WHERE email=?'
        user = conexao.execute(SELECT,(nome,)).fetchone()
        #user = conexao.execute('SELECT * FROM usuarios WHERE email=?', (nome,)).fetchone()

        if user and user['senha'] == senha:
        #if user and senha == senha:
            session['user'] = nome
            return redirect(url_for('dash'))
        else:
            return "SENHA INCORRETA ou não está cadastrado"

    

@app.route('/register', methods=['GET', 'POST'])
def register():

    # se já tá logado
    if 'user' in session:
        return redirect (url_for('dash')) #vai pra o dashboard

    if request.method == 'GET':
        return render_template('register.html')
    else:
        
        nome = request.form['nome']
        senha = request.form['senha']


        conexao = obter_conexao()
        SELECT = 'SELECT * FROM usuarios WHERE email=?'
        user = conexao.execute(SELECT,(nome,)).fetchone()
        #user = ('SELECT * FROM usuarios WHERE email=?',(nome,)).fetchone()

        if user and user['senha'] == senha:
            conexao.commit()
            conexao.close()

        else:
            #conexao = obter_conexao()
            INSERT = 'INSERT INTO usuarios(email,senha) VALUES(?,?)'
            conexao.execute(INSERT, (nome, senha))
            #conexao.execute("INSERT INTO usuarios(email, senha) VALUES (?,?)", (nome, senha))
            conexao.commit()
            conexao.close()


        session['user'] = nome
        return redirect(url_for('dash'))

        
@app.route('/logout', methods=['POST'])
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))
