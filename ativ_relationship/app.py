from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import Clientes, Veiculos, Locadora
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atv.db'

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email= request.form['email']
        senha= request.form['senha']
        
        return redirect(url_for('index'))
    
    return render_template('cadastrar_cliente.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        email= request.form['email']
        senha= request.form['senha']
        
        return redirect(url_for('index'))
    
    return render_template('cadastrar_cliente.html')




@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        novo_cliente = Clientes(nome=nome)
        db.session.add(novo_cliente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('cadastrar_cliente.html')

@app.route('/cadastrar_veiculo', methods=['GET', 'POST'])
def cadastrar_veiculo():
    if request.method == 'POST':
        modelo = request.form['modelo']
        novo_veiculo = Veiculos(nome=modelo)
        db.session.add(novo_veiculo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('cadastrar_veiculo.html')

@app.route('/cadastrar_locacao', methods=['GET', 'POST'])
def cadastrar_locacao():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        veiculo_id = request.form['veiculo_id']
        data = request.form['data']
        nova_locacao = Locadora(cliente_id=cliente_id, veiculo_id=veiculo_id, data=data)
        db.session.add(nova_locacao)
        db.session.commit()
        return redirect(url_for('index'))
    
    clientes = db.session.query(Clientes).all()   
    veiculos = db.session.query(Veiculos).all()
    return render_template('cadastrar_locacao.html', clientes=clientes, veiculos=veiculos)

@app.route('/listar')
def listar():
    clientes = db.session.query(Clientes).all()   
    veiculos = db.session.query(Veiculos).all()
    locacoes = db.session.query(Locadora).all()
    return render_template('listar.html', clientes=clientes, veiculos=veiculos, locacoes=locacoes)