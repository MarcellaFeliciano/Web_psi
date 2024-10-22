

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







