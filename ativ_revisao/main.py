from flask import Flask, request, render_template, abort

app = Flask(__name__) # a aplicação / responsavel por receber e enviar os https

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def pagina1():
    return render_template('index.html')
    
@app.route('/about')
def pagina2():
    return render_template('about.html')
    
@app.route('/dashboard')
def pagina3():
    return render_template('dashboard.html')

    
@app.route('/login', methods=['POST', 'GET']) # definir os metodos da aplicação
def login():
    if request.method == 'GET': # quando faço a solicitação get no /login eu recebo o login.html
        return render_template('login.html')
    elif request.method == 'POST': # o metodo request retorna o metodo
        email = request.form['email']  # pega os dados do usuario / ou seja ele pega no form o email
        senha = request.form['senha'] # request / form / name

        if email == 'admin@email.com' and senha == '123123':
            return render_template('cadastro.html')
        else:
            return render_template('error.html'), 401


@app.route('/cadastro', methods=['POST','GET'])
def cadastrar():
    if request.method =='GET':
        return render_template('cadastro.html')
    elif request.method == 'POST':
        
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']  # pega os dados do usuario / ou seja ele pega no form o email


