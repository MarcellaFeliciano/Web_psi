from flask import Flask, request, render_template, url_for


app = Flask (__name__) # criar aplicação flask


 # criar as rotas
@app.route('/')
def ola_mundo():
    return f"""
        <h1>oie mundo</h1> 
        <a href='{ url_for('pagina_sobre') }'>PAGINA SOBRE</a>
        """


@app.route("/sobre")
def pagina_sobre():

    # ?nome=jose
    nome = request.args.get('nome')
    return render_template('index.html', nome=nome)
    # retornar a pagina iindex.html com o dado romerito



