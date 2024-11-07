from flask import render_template, Blueprint, url_for, request, session, flash, redirect
from models.medico import Medico

# módulo de usuários
bp_medico = Blueprint(name='medicos', import_name=__name__, url_prefix='/medicos')

@bp_medico.route('/')
def index():
    if 'user' not in session:
        return render_template('medico/index.html', medicos = Medico.all())
    else:
        return render_template('medico/index.html', medicos = Medico.all(), nome=session['user'])


@bp_medico.route('/cadastrar', methods=['POST','GET'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        medico = Medico(nome=nome, email=email, senha=senha)
        medico.cadastrar()
    
        session['user'] = nome
        
        return redirect(url_for('medicos.index'))

    else:
        if 'user' not in session:
            return render_template('medico/cadastrar.html')

        else:
            return render_template('medico/cadastrar.html', nome=session['user'])




@bp_medico.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        nome = 'anonimo'
        email = request.form['email']
        senha = request.form['senha']

        medico = Medico(nome=nome, email=email, senha=senha)
        logado = medico.logar()       

        if logado:
            session['user'] = medico.nome
            return redirect(url_for('index'))
        else:
            message = 'Não foi possivel logar! '
            return render_template('medico/login.html', message = message)
        
    else:
        if 'user' not in session:
            return render_template('medico/login.html')
        else:
            return render_template('medico/login.html', nome=session['user'])


@bp_medico.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))