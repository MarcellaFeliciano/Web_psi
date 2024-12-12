from flask import Flask, render_template, request, make_response, redirect, url_for, session
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = 'muitodificil'


database = 'database/database.db'
def get_connection():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    if 'user' not in session:
        return render_template('index.html')
    else:
        nome = session['user']
        return render_template('index.html', nome=nome)

@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']


        conn = get_connection()  
        cursor = conn.cursor()  
        cursor.execute("INSERT INTO tb_users(nome, email, senha) VALUES (?,?,?)", (nome, email, senha))
        session['user'] = nome

        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    # retornar os dados do usuario cadsatrado

    else:
        if 'user' not in session:
            return render_template('cadastro.html')
        else:
            return render_template('cadastro.html', nome=session['user'])


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conn = get_connection()  
        cursor = conn.cursor()  

        cursor.execute("SELECT * FROM tb_users WHERE email = ?", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user['email'] == email and user['senha'] == senha:
            session['user'] = user['nome']
            return redirect(url_for('index'))
        else:
            return render_template('login.html', message='Email ou senha errados!')
    else:
        if 'user' not in session:
            return render_template('login.html')
        else:
            return render_template('login.html', nome=session['user'])


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))


@app.route('/registrar_pratos', methods=['POST','GET'])
def registrar_pratos():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        tipo = request.form['tipo']


        # não adicionei no dicionario pois utlizei o banco
        conn = get_connection()  
        cursor = conn.cursor()      
        cursor.execute("INSERT INTO tb_pratos(nome, preco, tipo) VALUES (?,?,?)", (nome, preco, tipo))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('registrar_pratos.html')


@app.route('/filtrar_pratos')
def filtrar_pratos():

    filtro = request.args.get('tipo')
    conn = get_connection()
    pratos = conn.execute("SELECT * FROM tb_pratos WHERE tipo = ?", (filtro,)).fetchall()
    conn.close()

    if pratos == None:
        conn = get_connection()
        pratos = conn.execute("SELECT * FROM tb_pratos").fetchall()
        conn.close()
        return render_template('filtrar_pratos.html', pratos = pratos, filtro=filtro)


    return render_template('filtrar_pratos.html', pratos = pratos, filtro=filtro)
