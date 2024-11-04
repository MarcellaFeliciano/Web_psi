from flask import render_template, Blueprint, url_for, request, flash, redirect

from models.emprestimo import Emprestimo
from models.user import User
from models.book import Book


# módulo de usuários
bp = Blueprint('emprestimos', __name__, url_prefix='/emprestimo')


@bp.route('/')
def index():
    return render_template('emprestimos/index.html', emprestimos =  Emprestimo.all())

@bp.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        user = request.form['user']
        book = request.form['book']
        data = request.form['data']

        emprestimo = Emprestimo(user, book, data)
        emprestimo.save()
        return redirect(url_for('emprestimos.index'))

    else:
        return render_template('emprestimos/register.html', users=User.all(), books=Book.all())
    

