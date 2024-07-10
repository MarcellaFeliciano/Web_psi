from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return "oi"

@app.route('/formulario', methods=['GET', 'POST'])
def form():

    if request.method == 'GET':
        return render_template('formulario.html')
    else:
        nome = request.form['name']
        return nome
    

@app.route('/dados')
def dados():

    nome = 'Romerito'
    return render_template("dados.html", nome=nome)


@app.route('/url')
def teste_url():
    return url_for('form') # a fução url_for leva ao link da função (def form)
