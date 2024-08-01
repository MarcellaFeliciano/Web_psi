from flask import Flask, session, request, render_template,url_for, redirect

app = Flask(__name__)

bancodados = {}

# chave para critografia de cookies na sessão
app.config['SECRET_KEY'] = 'superdificil'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dash():

    if 'user' not in session:
        return redirect(url_for('index'))

    return render_template('dashboard.html', nome=session['user']) # pega o valor salvo no cookie da sessão

@app.route('/login', methods=['GET','POST'])
def login():
     # se tentar acessar o login já estando logado!
    if 'user' in session:
        return redirect(url_for('dash'))

    if request.method == 'GET':
        return render_template('login.html')
    else:
        # fazer o login - POST - receber dados
        nome = request.form['nome']
        senha = request.form['senha']

        # se os dados do login estão cadastrados o usuario pode ir para o dash
        if nome in bancodados and bancodados[nome] == senha:
            session['user'] = nome
            return redirect(url_for('dash'))

        else:
            # caso o login do usurairo não estiver cadastrado ou a senha do usurario que está cadastrado está erradpo! 
            return render_template('erro_login.html')
    

    return render_template('login.html')


@app.route("/logout", methods=['POST'])
def logout():
    if 'user' in session:
        session.pop('user', None)
        return redirect(url_for('index'))




@app.route('/register', methods=['GET','POST'])
def register():
    # se tentar acessar o cadastro já estando logado!
    if 'user' in session:
        return redirect(url_for('dash'))

    # entrar na pagina de registro
    if request.method == 'GET':
        return render_template("register.html")

    else:
        # fazer o cadastro - POST - receber dados
        nome = request.form['nome']
        senha = request.form['senha']

        if nome not in bancodados:
            # se o usuario ainda não está cadastrada no dicionario/banco de dados
            bancodados[nome] = senha
        
        else:
            return redirect(url_for('login'))

        # se o usuario está cadastrado significa que ele pode seguir para o dashboard
        session['user'] = nome # vai inicializar uma sessão que guardará um cookie na pagina web - saivando como ususario cadastrado igual o ultimjo usuario salvo ! o user
        return redirect(url_for('dash'))

