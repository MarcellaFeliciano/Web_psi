from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def index ():
    return render_template('auth/login.html')


@app.route('/dashboard')
def dashboard(): 
    return render_template('pages/dashboard.html')


@app.route('/dashboard/content')
def content():
    contents = [
        'texto sobre flask',
        'vídeo sobre templates',
        'código sobre css com flask'
    ]
    return render_template('pages/content.html', contents=contents)

@app.route('/')
def nome():
    nome = 'Bob'
    return "Bem vindo, " + nome.upper()