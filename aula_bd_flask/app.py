from flask import Flask, url_for, request, render_template, flash, redirect
import sqlite3

app = Flask(__name__)

# Obter conecção com o SQLITE
def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # essa classe linha retorna a chave e o valor
    return conn

@app.route('/')
def index():
    conn = get_connection()
    users = conn.execute("SELECT id, email FROM users").fetchall()
    return render_template('pages/index.html', users=users)

@app.route('/create', methods=['GET','POST'])
def create():

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']
        if not email:
            flash("Email é obrigatório!") # função do flask 
            
        else:
            conn = get_connection()
            conn.execute("INSERT INTO users (email, senha) VALUES(?,?)", (email, senha))
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template('pages/create.html')

# rota dinanmica ( id = int valor numerico = paramentro - associado a rota --> /1/edit)
@app.route('/<int:id>/edit', methods=['POST','GET'])
def edit(id):
    
    
    select = "SELECT * FROM users WHERE id=?"
    conn = get_connection()
    user = conn.execute(select,(str(id))).fetchone()

    if user == None:
        return "não existe"

    #return dict(user) # como dicionario 
    #return user.keys()

    

    if request.method == 'POST':

        email = request.form['email']
        update = "UPDATE users SET email=? WHERE id=?" 
        conn.execute(update, (email, id))

        conn.commit()
        conn.close()
  
        return redirect(url_for('index'))
    # editar uma coluna - fazer a mudança e fazer o commit e fechar a conecçaõ
    
 
    return render_template('pages/edit.html', user=user)
