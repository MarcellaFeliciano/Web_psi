

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













