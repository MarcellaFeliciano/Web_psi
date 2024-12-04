
from flask import render_template, Blueprint, url_for, request, flash, redirect

from models.users import User


# módulo de usuários
bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/')
def index():
    users = User.all()
    return render_template('pages/index.html', users=users)

@bp.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']

        if not email:
            flash('Email é obrigatório')
        else:
            User.add_user(email=email,senha=senha)
            return redirect(url_for('users.index'))
    
    return render_template('pages/create.html')

@bp.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):

    user = User.get_user(id)
    # Busca o usuário pelo ID ou retorna 404 se não encontrado
    if user == None:
        return redirect(url_for('error', message='Usuário Inexistente'))

    if request.method == 'POST':
        email = request.form['email']
        User.edit_email(id=id, email=email)
        return redirect(url_for('users.index'))
    
    return render_template('pages/edit.html', user=user)

@bp.route('/error')
def error():
    error = request.args.get('message')
    return render_template('errors/error.html', message=error)