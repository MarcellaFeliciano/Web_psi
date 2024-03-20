from flask import Flask, request, render_template, abort
from faker import Faker # iniciar o faker para gerar nome de pessoasq/emais e etc de coisas reiais
# util para testar aplicações

app = Flask(__name__) # a aplicação / responsavel por receber e enviar os https

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET']) # definir os metodos da aplicação
def login():
    if request.method == 'GET': # quando faço a solicitação get no /login eu recebo o login.html
        return render_template('login.html')
    elif request.method == 'POST': # o metodo request retorna o metodo
        email = request.form['email']  # pega os dados do usuario / ou seja ele pega no form o email
        senha = request.form['senha'] # request / form / name

        if email == 'admin@email.com' and senha == '123123':
            return render_template('dashboard.html')
        else:
            return render_template('errors/401.html'), 401

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/buscar')
def search():
    lista = ['livro', 'pc', 'camisa', 'relogio']
    item = request.args.get('item')
    # o request recebe o dado do formularo
    
    if item == None:
        return render_template('errors/400.html'), 400
    
    resultado = {}    
    if item in lista:
        faker = Faker(locale="pt_BR") # em portugues
        for x in lista:
            resultado[x] = [ faker.job() for y in range(50) ] # vou gerar 50 valores - preparo o resutado 
        return render_template('produtos.html', produtos=resultado[item])
    else:
        return render_template('produtos.html', produtos=[])
        
        

    