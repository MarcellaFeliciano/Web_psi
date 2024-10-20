from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = 'senha'


# Configurações do MySQL
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'marcella123'
app.config['MYSQL_DB'] = 'db_ativ_revisao'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    if 'user' not in session:
        return render_template('index.html')
    else:
        nome = session['user']
        
        return render_template('index.html', nome=nome)


@app.route('/login', methods=['POST','GET'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tb_users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user['email'] == email and user['senha'] == senha:
            session['user'] = user['nome']

            return redirect(url_for('index'))
        else:
            flash('Email ou senha errados!')
    else:
        if 'user' not in session:
            return render_template('login.html')
        else:
            return render_template('login.html', nome=session['user'])

@app.route('/registrar', methods=['POST','GET'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        cursor = mysql.connection.cursor()

        cursor.execute("SELECT * FROM tb_users")
        user_email = cursor.fetchall()  # Use fetchone() para obter um único registro
        cursor.close()

# perguntar (select) se o email que vai ser salvo já existe no banco : se sim = não cadsatra

        for i in user_email:
            if i['email'] == email:
                resu = 'cadastrado'
            else: 
                resu = 'não cadastrado'
                
        if resu == 'não cadastrado':

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO tb_users(nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
            mysql.connection.commit()
            cursor.close()

            session['user'] = nome
            return redirect(url_for('dash'))
         # retornar os dados do usuario cadsatrado

        else:
            menssagem = 'Email já cadastrado!'
            return render_template('registrar.html', nome=nome, menssagem = menssagem)
    else:
        if 'user' not in session:
            return render_template('registrar.html')
        else:
            return render_template('registrar.html', nome=session['user'])


@app.route('/dash')  # mostrar link para ir para adicionar
def dash():
    if 'user' not in session:
            return render_template('index.html')
    else:
        return render_template('dash.html', nome = session['user'])   


@app.route('/adi_info', methods=['POST','GET']) # Adicionar informaçções de quem está logado
def adi_info():
    if request.method == 'POST':

        cursor = mysql.connection.cursor()
        nome = session['user']
        cursor.execute("SELECT * FROM tb_users WHERE nome = %s", (nome,))
        user = cursor.fetchone()  # Use fetchone() para obter um único registro
        cursor.close()
        id = user['id']

        nome_completo = request.form['nome']
        genero = request.form['genero']
        data_nasc = request.form['data_nasc']
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO tb_info_users(nome_completo, genero, data_nasc, endereco, telefone, id_user) VALUES (%s, %s, %s, %s, %s, %s)", (nome_completo, genero, data_nasc, endereco, telefone, id))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('perfil'))

    else:
        return render_template('adi_info.html', nome = session['user'])

@app.route('/pesquisar', methods=['POST','GET']) # pesquisar algum usuario
def pesquisar():
    if request.method == 'POST':
        nome = request.form['nome']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT nome_completo, email, genero, data_nasc, endereco, telefone FROM tb_users JOIN tb_info_users on id_user = id WHERE nome = %s", (nome,))
        user = cursor.fetchone()  # Use fetchone() para obter um único registro
        cursor.close()

        return render_template('pesquisar.html', user=user, nome=session['user'])

    else: 
        if 'user' not in session:
            return render_template('pesquisar.html', user=None)
        else:
            return render_template('pesquisar.html', user=None, nome=session['user'])





@app.route('/perfil')
def perfil():
    if 'user' not in session:
            return render_template('index.html')
    else:  
        nome = session['user']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT nome_completo, email, genero, data_nasc, endereco, telefone FROM tb_users JOIN tb_info_users on id_user = id WHERE nome = %s", (nome,))
        user = cursor.fetchone()  # Use fetchone() para obter um único registro
        cursor.close()

        return render_template('perfil.html', nome = nome, user = user)

@app.route('/edi_info', methods=['POST','GET'])
def edi_info():
    if request.method == 'POST':
            
        nome = session['user']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tb_users WHERE nome = %s", (nome,))
        user = cursor.fetchone()  # Use fetchone() para obter um único registro
        cursor.close()
        id = user['id']

        nome_completo = request.form['nome']
        genero = request.form['genero']
        data_nasc = request.form['data_nasc']
        endereco = request.form['endereco']
        telefone = request.form['telefone']

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE tb_info_users SET nome_completo = %s, genero = %s, data_nasc = %s, endereco = %s, telefone = %s WHERE id_user = %s", (nome_completo, genero, data_nasc, endereco, telefone, id))
        user = cursor.fetchone()  # Use fetchone() para obter um único registro
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('perfil'))
    
    else:
        return render_template('edi_info.html', nome=session['user'])


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))