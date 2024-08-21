from flask import Flask, url_for, request, render_template, flash, redirect
import sqlite3

app = Flask(__name__)

# Obter conecção com o SQLITE
def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
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

# 
@app.route('/<int:id>/edit')
def edit(id):

    # editar uma coluna - fazer a mudança e fazer o commit e fechar a conecçaõ
    conn = get_connection()
    update = "UPDATE users SET email=? WHERE ID=?"
    conn.execute(update, (novo_email, id))
    return str(id)

