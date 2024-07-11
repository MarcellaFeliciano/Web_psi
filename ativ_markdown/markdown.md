# Atividade de Programação de Sistemas para Internet

##  Pesquisa sobre o uso de Cookies e Sessions em flask.

# Cookies:

> Cookies são pequenos pedaços de dados armazenados no navegador do usuário pelo site. Eles são usados para armazenar informações, como preferências, identificações de login e outras finalidades relacionadas a interação com o site.
>

### Configurando cookies no Flask:

>Para definir um cookie em Flask, você normalmente utiliza a função **make_response()** que serve para criar uma resposta, e então chama **set_cookie()** no objeto de resposta para definir o cookie que será armazenado.

>

## Código de exemplo com Cookies
```
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Assume que o nome de usuário é enviado por um formulário POST
    usuario = request.form['usuario'] 
    
    # Define um cookie com o nome 'usuario' e valor igual ao nome de usuário
    resposta = make_response('Login bem-sucedido!')
    resposta.set_cookie('usuario', usuario)
    return resposta

@app.route('/profile')
def profile():
    # Recupera o valor do cookie 'usuario'
    usuario = request.cookies.get('usuario')
    return f'Bem-vindo ao seu perfil, {usuario}!'


@app.route('/')
def set_cookie():
    response = make_response('Cookie definido!')
    response.set_cookie('username', 'john')
    return response
```
## Informações sobre os Cookies

* **Segurança:** Não armazene informações sensíveis nos cookies, pois eles podem ser acessados e modificados pelo usuário.
* **Tamanho:** Cookies têm limitações quanto ao seu tamanho, então evite armazenar grandes quantidades de dados.
* **Privacidade:** Certifique-se de estar em conformidade com regulamentos de privacidade ao utilizar cookies para rastrear usuários.


# Sessions:
>As sessions em Flask são usadas para armazenar informações do usuário de forma persistente durante várias requisições. Diferente dos cookies, onde os dados são armazenados no navegador do cliente, as sessions são gerenciadas no lado do servidor.
>

## Introdução a Sessions no Flask

### Inicialização da chave secreta

> Para inicializar sessões você precisa configurar uma chave secreta no seu aplicativo usada para criptografar e descriptografar os dados da sessão. Isso é feito definindo 'app.secret_key' .

##### Código de configuração da chave secreta
```
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'chave_secreta'

```

### Armazenamento de dados
> Para armazenar dados na sessão, você usa 'session['chave'] = valor'.
>

##### Código armazenamento dos dados
```
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    session[''usuario'] = 'usuario
    return 'Login bem-sucedido!'
```
### Acessar os dados
>Para acessar os dados da sessão, você usa session['chave'].
>


##### Código para acessar os dados
```
@app.route('/profile')
def profile():
    if 'usuario' in session:
        return f'Bem-vindo, {session["usuario"]}!'
    else:
        return 'Você não está logado.'
```

### Remover os dados
>Para remover dados da sessão, você pode usar 'session.pop('chave', None)'.
>

##### Código para remover os dados
```
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return 'Logout realizado com sucesso!'
```

### Importante

> As sessões são temporárias e duram enquanto o usuário está interagindo com o aplicativo. Se o usuário fechar o navegador ou a sessão expirar (por configuração), os dados da sessão são perdidos.
>