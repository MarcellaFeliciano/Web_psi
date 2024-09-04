from flask import Flask
from werkzeug.security import check_password_hash, generate_password_hash




"""
from werkzeug.security import generate_password_hash
generate_password_hash('123')

hash = generate_password_hash('123')

>>> from werkzeug.security import check_password_hash

>>> check_password_hash(hash, '123')
True
>>> check_password_hash(hash, '1234')
False




https://flask-login.readthedocs.io/en/latest/


flask-login - ajuda a gerenciar o ligin no flask 

- utiliza uma class (User) com heranca na classe do pacote de login-flask
precisa de propriedades especificas :

is_authenticated
This property should return True if the user is authenticated

is_active
This property should return True if this is an active user 

is_anonymous
This property should return True if this is an anonymous user.

get_id()
This method must return a str that uniquely identifies this user

-> encapsula a função de mostarr a senha
@property
def _password(self)
    return self._hash

--> propriedade que quando eyu trentar chmar a senha eu mostrarei o hash  / logo a variavel password será temporarua

user._password ='12'
print(user._password)

-> mostrará o hash



"""


app = Flask(__name__)