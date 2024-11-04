from flask import render_template, Blueprint, url_for, request, flash, redirect
from models.user import User

# módulo de usuários
bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/')
def index():
    return render_template('users/index.html', users = User.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nome= request.form['nome']

        if not email:
            flash('Email é obrigatório')
        else:
            user = User(email, nome)
            user.save()
            return redirect(url_for('users.index'))
    
    return render_template('users/register.html')

