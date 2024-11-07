from flask import render_template, Blueprint, url_for, request, flash, redirect, session
from models.paciente import Paciente

# módulo de usuários
bp_paciente = Blueprint(name='pacientes', import_name=__name__, url_prefix='/pacientes')

@bp_paciente.route('/')
def index():
    if 'user' not in session:
        return render_template('paciente/index.html', pacientes = Paciente.all())
    else:
        return render_template('paciente/index.html', paciente = Paciente.all(), nome=session['user'])


@bp_paciente.route('/registrar', methods=['POST','GET'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        idade = request.form['idade']
        telefone = request.form['telefone']

        paciente = Paciente(nome=nome, genero=genero, idade=idade, telefone=telefone)
        paciente.registrar()

        return redirect(url_for('pacientes.index'))

    else:
        if 'user' not in session:
            return render_template('paciente/registrar.html')

        else:
            return render_template('paciente/registrar.html', nome=session['user'])


