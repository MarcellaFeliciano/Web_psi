from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    # verifica se existe cookie, que será utlizado para colorir a pagina,
    if 'color' in request.cookies:
        return render_template('index.html', cor=request.cookies['color'])

    # se não existe cookie ele irá mostrar a pagina inicial com a cor (variavel) igual a branco
    return render_template('index.html', cor='white')

@app.route("/color")
def color():
# a informação do select (que irá pegar a option escolhida) esta definido com o name = 'color
    cor = request.args.get('color')
    # Quando enviamos dados via GET como no exemplo das cores, podemos usar o atributo request.args do objeto request para obter os dados enviados.

    # verifica se existe o cookie  - a chave do cookie é 'color'!
    if 'color' in request.cookies: # se existir cookie
        if cor != request.cookies['color']: 
            # se o cookie for difenrete eu altero a prefernciad de cor

            # definir novo cookie
            template = render_template('color.html', cor=cor)
            response = make_response(template)
            response.delete_cookie("color")
            response.set_cookie("color", value=cor)
            return response

        else:
            # se o cookie for igual não há mudança na cor do cookie armazenado
            return render_template("color.html", cor=request.cookies['color'])


    else:
        # a variavel template = (a pagina html que será aberta como resposta, recebendo a varivel cor= a cor escolhida)
        template = render_template('color.html', cor=cor)
        
        # faço a resposta com o arquivo html e a cor (variavel cor que será enviada ao html para ser usada no body )
        response = make_response(template)
        response.delete_cookie("color") # desnecessario pois o cookie ainda não existe

        # crio o cookie  (chave = 'color' e o valor do cookie = cor)
        response.set_cookie("color", value=cor)
        return response

    return render_template('color.html', cor=request.cookies['color'])


