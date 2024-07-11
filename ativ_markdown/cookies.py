from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']  # Assume que o nome de usuário é enviado por um formulário POST

    # Define um cookie com o nome 'usuario' e valor igual ao nome de usuário
    
    resposta = make_response('Login bem-sucedido!')
    resposta.set_cookie('usuario', usuario)
    return resposta

@app.route('/profile')
def profile():
    # Recupera o valor do cookie 'usuario'
    usuario = request.cookies.get('usuario')
    return f'Bem-vindo ao seu perfil, {usuario}!'

