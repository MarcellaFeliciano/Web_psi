

# CONTEÚDO DE PSI

## MVC - MODEL / VIEW / CONTROLL

```

user -----> VIEW  ()
            ^  I
            I  v
          CONTROLLER  (CONTROLA OS REQUESITOS)
            ^  I
            I  v
            MODEL     <-------->       BASE DE DADOS
(MODELO QUE GERENCIA OS DADOS E FUNÇÕES)   (Solicitação de dados e respostas do BD)
```


EXEMPLO
```

 > controllers
 > database
 > env
 > models  -> user.py (classe do bd) guardará as funções relacionadas a classe
 > templates
 __init__.py (todas as pastas tem esse arquivo - __init__ serve para reconhecer que é um pacote)
 .getignome
  app.py
> img

```
- Começar pelo controlador
- Fazer os templates
- fazer o banco de dados
- fazer o modelo
  



```python
- user.py -    (MODEL RELACIONADO AO USUARIO)
from case2.database import get_connection

class User:
  def __init__(self,email)
    self.email = email

```

```python
- __init__.py  ( arquivo que inicializa o app do flask)
from flask import Flask
app = Flask()
```
```python
- app.py
from case2 import app  (estou importando  a variavel app que está no arquivo __init__)
from case2.controllers import UserCOntroller
```

```python
- usercontroler
nele ficará as rotas (views) que controlam os pedidos do user -> controla o que a camada de modelo irá fazer por meio das funções e classes

from flask import render_template, redirect, url_for, reuquest, flask
from case2 import app
from case2.database import get_connetiom
from case2.models.user import User

@app.route(/index)
def index()

```


## Blueprint

> Um Blueprint no Flask é uma maneira de organizar e modularizar diferentes partes da sua aplicação, agrupando um conjunto de views, rotas, e outros componentes relacionados em um único local. Ele  >permite separar funcionalidades da aplicação em seções independentes, facilitando a manutenção e a escalabilidade do código.


- Organização Modular: Em vez de registrar rotas e views diretamente no objeto da aplicação Flask, você cria um Blueprint para organizar essas partes da aplicação em módulos separados. 

- Facilidade de Registro: Você pode definir múltiplos Blueprints para diferentes funcionalidades e, em seguida, registrá-los todos na aplicação principal quando ela é inicializada. Isso é feito na função de fábrica (create_app()), o que permite que seu código seja facilmente configurado e modificado sem a necessidade de mexer diretamente na aplicação principal.


#### Exemplo

```python
from flask import Blueprint

# Criando o Blueprint de autenticação
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Definindo uma rota dentro do Blueprint
@bp.route('/login', methods=['GET', 'POST'])
def login():
    # lógica da view de login
    return "Login Page"

# No arquivo principal da aplicação (__init__.py), registre o Blueprint
def create_app():
    app = Flask(__name__)
    # Registrar o Blueprint auth
    app.register_blueprint(auth.bp)

    return app


```


from flask import Flask, render_template

from users import users
from books import books

app = Flask(__name__, template_folder='templates')

app.register_blueprint(users.bp)
app.register_blueprint(books.bp)



templates/
templates/users
templates/books


bp = Blueprint('users', name __name__, url_prefix =


__init__.py --> 

__all__ = [
'users',
'models'
]
declara os pacotes, onde eu posso -> from users import *


### Blueprint Caso 2

> app.py
```python
from flask import Flask
from controllers import users, books

app = Flask(__name__)
app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
```
> controllers
> __init__.py
```python
all = [
    'books',
    'users'
]
```
> users.py
```python
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
```
> books

```python
from flask import Flask, render_template, url_for, request, Blueprint, redirect
from models.user import User
from models.book import Book

bp = Blueprint('books', __name__, url_prefix='/books')

@bp.route('/')
def index():
    return render_template('books/index.html', books = Book.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        titulo = request.form['titulo']
        user = request.form['user']

        book = Book(titulo, user)
        book.save()
        return redirect(url_for('books.index'))


    return render_template('books/register.html', users=User.all())

```

> models
>__init__.py
```python
__all__ = [
    'user',
    'book'
]
```
> books.py

```python
from database import get_connection

class Book:
    def __init__(self, titulo, user_id):
        self.titulo = titulo
        self.user_id = user_id

    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO books(titulo, user_id) values(?,?)", (self.titulo, self.user_id))
        conn.commit()
        conn.close()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        books = conn.execute("SELECT * FROM books").fetchall()
        return books
```
> users.py
```python
from database import get_connection

class User:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO users(email, nome) values(?,?)", (self.email, self.nome))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT * FROM users").fetchall()
        return users

```




## SQL ALCHEMY

- Classes de metodo não precisam que o objeto esteja instanciado a classe, já as outras funlções são ligadas ao objeto

```python
from sqlalchemy import create_engine, Integer, ForeignKey
from sqlalchemy.orm import Session # manipular sessão
from sqlalchemy.orm import DeclarativeBase #base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from sqlalchemy import select

class Base(DeclarativeBase):
    pass


# modo declarativo
# quando a classe herda a classe base o banco entende que elas estão relacionadas
class User(Base):
    __tablename__ = 'user' # exite a tabela / cria a tabela no modelo

    # estou mapeando no banco de dados que o atributo/coluna id será do tipo int - definir / declarar no modelo o atributo
    id: Mapped[int] = mapped_column(primary_key=True) 
    nome: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True) # só pode ocorrer uma vez o valor
    books: Mapped[List['Book']] = relationship() # relacionamento de 1 para M Pois o user tem varios lviros

    def __repr__(self): # formatar o print do select/ objeto representado em string
        return f"(nome={self.nome}, email={self.email})"



class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    author: Mapped[str] = mapped_column(ForeignKey('user.id'))


engine = create_engine('sqlite:///teste.db') # fabrica de conexão com o banco

session = Session(bind=engine) # sessão que manipula os dados do banco

# criar o banco
Base.metadata.create_all(engine)

# Adicionar user
usuario = User(nome='marcella', email='evely@g')
session.add(usuario)
session.commit()

#declaracao = select(User) # o select prepara a operação sql (select * from tb da classe User)
#print(declaracao)



sql = select(User)
lista = session.execute(sql)
print(lista)

for user in lista:
    print(user)

sql_filtro = select(User).where(User.email == 'evely@g')
resutado = session.execute(sql_filtro)

print(resutado.all())

sql_filtro2 = select(User.email).where(User.email == 'evely@g')
resutado = session.execute(sql_filtro2)
print(resutado.all())
```
