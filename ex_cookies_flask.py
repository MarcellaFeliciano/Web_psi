from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def homepage():
  return "Meu site está no ar"

# quando entro nessa pagina (criar cookie) ele cria um dicionario com os dados 
@app.route("/criar-cookie")  
def criar_cookie():
  resposta = make_response("O cookie foi criado")  # posso direcionar a paginas html ou mensagens
  resposta.set_cookie("nome_usuario", "Lira")  #dicionario
  resposta.set_cookie("idade", "19") 
  return resposta

# quando entro nessa pagina (ver cookie) ele mostra o dicionario que foi criado / se o cookie ainda não tiver sido criado o dicionario estará vazio -> {}
@app.route("/ver_cookie") 
def ver_cookie():
  cookies = request.cookies  # nome_usuario = cookies.get("nome_usuario")
  return cookies
  
