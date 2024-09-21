from flask import Flask
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL


app = Flask(__name__)

mysql = MySQL(app)

cursor = mysql.connection.cursor()
"""
class User(UserMixin): 
id : str    # ele obrigatoriamente tem que ser string
    def __init__(self,nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
"""