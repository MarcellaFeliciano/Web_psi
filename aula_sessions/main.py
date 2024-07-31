from flask import Flask, render_template, url_for, request, make_response

"""
- adicionar mensagens
- mensagens vinculadas por usuario
- filtrar mensagem por usuario
- utilizar cookies

app.config['SECRET KEY'] = '123123'

@app.route('/')
def teste():
    session['name'] = 'marcella'
    return render_template('index.html')
"""

app = Flask(__name__)

# nosso 'banco de dados'    
mensagens = {}  # variavel para guradar as info/requisições
# as requisiçoes sao indepoenddertes uma das outras / o methpod http só tem informação do qu efoi pedido no momento, por isso é dificil manter infromações - surge os cookies (para manter informações)


"""   UM DIXIONARIO COM CHAVE DOS USUARIOS E UMA LISTA COMO VALOR PARA GURADRA AS MENSAGENS
{
'romerito' ['a', 'b']
'JV' ['C']

}
"""
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mensagem')
def mensagem():
    return render_template('mensagem.html')


@app.route('/mural', methods=['GET','POST'])
def mural():
    #processar o recebimento de novas mensagens
    if request.method == 'POST':
        #um usurario mandoi mensagem
        name = request.form['name']
        message = request.form['message']


        if name in mensagens:
            mensagens[name].append(message) # SE  EXISTIR UMA CHAVE COM ESSE USUARIO SALVO EU ADICIONO A MENSASSEGM NA LISTA REFERENTE A CHAVE DO USUARIO
        
        else:
            mensagens[name] = [message]  # SE AINDA NÃO EXISTIR O USUARIO ELE CRIA UMA CHAVE COM O NOME E ADICIONA A MENSAGEM COMO LISTA = [MESSAGE]
        
        # lista mensagens sd eum usurario ativo 

        if 'nome' in request.cookies and request.cookies['nome'] == name:  #se o nome estiver em cookie
            return render_template('mural.html', lista=mensagens[name])
        else:
            template = render_template('mural.html', lista=mensagens[name])
            response = make_response(template) 
            response.set_cookie(key='nome', value=name)

            return response

    else: # se o method for get (o usuario deu f5 e iintrou em mural - o seite esta cadastrado com o cookie do ultimo usuario!)
        lista = []
        if 'nome' in request.cookies:
            name = request.cookies['nome']
            
            if name in mensagens:
                lista = mensagens[name]

        return render_template('mural.html', lista=lista)





"""
from flask import Flask, session

# sessoes são controladas pelo framework muita mais seguras e confiaveis, os dados (login e usuario / logout) são armazenados por um tempo predefinido
# ao ativar uma sessão eu crio um 'cookie' que será gurdado pelo tempo determinado 
# utilizado para proteger rotas

app.config['SECRET KEY'] = 'seper dificil de encontrar'

@app.route('/')
def index():
    session['user'] = 'romerito'
    return 'oi sessão criada'

@app.route('/jose')
def jose():
    if 'user' in session and session['user'] == 'jose':  # só posso utilizar a sessão se o nome definido no user da sessão for igual
        return 'fala ze'
    return redirect(url_for(index.html))  # o redirect pode ser utlizado para trafegar dados entre as paginas html / no caso ele está redirecionando  para a pagina index
    

"""