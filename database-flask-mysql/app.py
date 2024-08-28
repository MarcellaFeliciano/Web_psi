from flask import Flask, request, render_template, \
    redirect, url_for, flash

from flask_mysqldb import MySQL

app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PORT'] = '3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'romerito'
app.config['MYSQL_DB'] = 'users'
# retornar os dados como discionários
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# habilitar mensagens flash
app.config['SECRET_KEY'] = 'muitodificil'

@app.route('/')
def index():
    conn = mysql.connection.cursor()
    conn.execute("""SELECT * FROM users""")
    users = conn.fetchall()
    return render_template('pages/index.html', users=users)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        email = request.form['email']
        senha= request.form['password']

        if not email:
            flash('Email é obrigatório')
        else:
            conn = mysql.connection.cursor()
            conn.execute("INSERT INTO users(email, senha) VALUES (%s,%s)", (email, senha))
            mysql.connection.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('pages/create.html')

@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):

    # obter informação do usuário
    conn = mysql.connection.cursor()
    conn.execute('SELECT id, email, senha FROM users WHERE id = %s', (str(id)))
    user = conn.fetchone()

    if user == None:
        return redirect(url_for('error', message='Usuário Inexistente'))

    if request.method == 'POST':
        email = request.form['email']

        conn.execute('UPDATE users SET email=%s WHERE id=%s', (email, id))
        mysql.connection.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('pages/edit.html', user=user)

@app.route('/error')
def error():
    error = request.args.get('message')
    return render_template('errors/error.html', message=error)