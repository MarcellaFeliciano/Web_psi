from flask import Flask, request, render_template

app = Flask(__name__) # a aplicação / responsavel por receber e enviar os https

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET']) # definir os metodos da aplicação
def login():
    if request.method == 'GET': # quando faço a solicitação get no /login eu recebo o login.html
        return render_template('login.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        num_conv = request.form['num_conv']

        

        return render_template('enviado.html')

