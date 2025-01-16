from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from models import User
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    user = User(nome='Marcella')

    db.session.add(user)
    db.session.commit()

    return render_template('listar.html')

@app.route('/listar')
def listar():
    resutado = db.session.execute(db.select(User)).scalars()
    return render_template('listar.html', resutado=resutado)