from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    session['usuario'] = 'usuario
    return 'Login bem-sucedido!'
    
@app.route('/profile')
def profile():
    if 'usuario' in session:
        return f'Bem-vindo, {session["usuario"]}!'
    else:
        return 'Você não está logado.'

def logout():
    session.pop('usuario', None)
    return 'Logout realizado com sucesso!'