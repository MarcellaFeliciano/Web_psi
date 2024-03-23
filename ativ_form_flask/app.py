
from flask import Flask, request, render_template
from faker import Faker

app = Flask(__name__) # a aplicação / responsavel por receber e enviar os https
bd = []
cont = 0


@app.route('/', methods=['POST', 'GET'])
def index():
    global bd
    global cont
    #return render_template('index.html')

    if request.method == 'GET': # quando faço a solicitação get no /login eu recebo o login.html
        return render_template('index.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        num_conv = request.form['num_conv']

        if nome == '' or email == '' or num_conv == '':
            return render_template('errors/401.html'), 401
        else:
            cont += 1
            bd.append({'nome':nome, 'email':email, 'num':int(num_conv)})
            print(bd)

            convidados = 0
            for c in bd:
                print(c['num'])
                convidados += c['num']
                print(convidados)
                
                
            return render_template('enviado.html', convidados = convidados)
        
@app.route('/lista_convidados')
def lista():
    global bd
    print(bd)
    lista_convidados = bd
    return render_template('lista.html', lista_convidados = lista_convidados)
