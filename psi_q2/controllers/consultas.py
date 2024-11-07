from flask import render_template, Blueprint, url_for, request, flash, redirect
from models.consulta import Consulta

# módulo de usuários
bp_consulta = Blueprint(name='consultas', import_name=__name__, url_prefix='/consultas')

@bp_consulta.route('/')
def index():
    return render_template('consulta/index.html', consultas = Consulta.all())

