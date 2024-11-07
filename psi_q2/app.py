
from flask import Flask, render_template, session
from controllers import consultas, medicos, pacientes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'senha'

app.register_blueprint(consultas.bp_consulta)
app.register_blueprint(medicos.bp_medico)
app.register_blueprint(pacientes.bp_paciente)


@app.route('/')
def index():
    if 'user' not in session:
        return render_template('index.html')
    else:
        nome = session['user']
        return render_template('index.html', nome=nome)
