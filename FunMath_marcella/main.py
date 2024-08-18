from flask import Flask, request, make_response, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

app.config['tempo_de_expiracao_quiz'] = 62  # 1 minute
app.config['pergunta_atual'] = 0

perguntas = ['Quando Felipe tinha 5 anos, o pai dele tinha 36 anos. Agora Felipe tem a metade da idade do pai. Quantos anos Felipe tem?',
             'Observando a sequência, o número que substitui a interrogação é? 1, 7, 6, – 1, – 7, – 6, 1, 7, 6, ?',
             'Qual é o sucessor do sucessor de 199?',
             'Qual é o antecessor do sucessor de 45?',
             'O valor da expressão (100 - 40) : 3 é:',
             'Em um anfiteatro, as cadeiras estão dispostas em 20 linhas e 15 colunas. Qual é o número total de cadeiras?',
             'Carlos guardou sua coleção de latas de refrigerante em casa. Em cada caixa couberam 28 latas. Ele usou 7 caixas e sobraram 6 latas de refrigerante. Quantas latas tem a coleção de Carlos?',
             'Arrumando 512 cadernos em 12 pacotes de mesma quantidade, sobraram ainda 8 cadernos. Quantos cadernos foram colocados em cada pacote?',
             'Um granjeiro tem 3 333 ovos para vender. Se colocar 33 ovos em cada caixa, quantas caixas completas vão formar?',
             'Alvimar pagou uma compra de R$ 3,50 com uma nota de R$ 5,00 e recebeu o troco em moedas de R$ 0,25. Quantas moedas ele recebeu?'
             ]

opcoes = [['18 anos', '24 anos', '31 anos', '36 anos'], 
          ['1', '-7', '6', '-1'], 
          ['199', '200', '201', '202'],
          ['44','45','46','47'],
          ['10','15','20','24'],
          ['35','150','200','300'],
          ['194','196','202','238'],
          ['28','36','42','48'],
          ['100','101','110','111'],
          ['4','5','6','7']
          ]

respostas = ['31 anos', '-1', '201','45','20','300','202','42','101','6']

@app.route('/')
def Index():
    return render_template('inicial.html')

@app.route('/login')
def Login():
    return render_template('login.html')

@app.route('/quiz', methods=['POST', 'GET'])
def Quiz():
    if request.method == 'POST':
        pergunta_atual = app.config['pergunta_atual']
        # Obter a resposta do usuário
        resposta_user = request.form.get('resposta')
        if resposta_user is None:
            # Error handling if the user doesn't select any option
            mensagem = "Por favor, selecione uma resposta."
            response = make_response(render_template('jogo_quiz.html', pergunta=perguntas[pergunta_atual], opcoes=opcoes[pergunta_atual], mensagem=mensagem))
            response.set_cookie('pergunta_atual', str(pergunta_atual))
            return response
        else:
            # Verificar se a resposta está correta
            if resposta_user == respostas[pergunta_atual]:
                # Passar para a próxima questão
                pergunta_atual += 1
                app.config['pergunta_atual'] = pergunta_atual
                if pergunta_atual < len(perguntas):
                    mensagem = "Parabéns! Sua resposta está correta."
                    response = make_response(render_template('jogo_quiz.html', pergunta=perguntas[pergunta_atual], opcoes=opcoes[pergunta_atual], mensagem=mensagem))
                    response.set_cookie('pergunta_atual', str(pergunta_atual))
                    response.set_cookie('tempo_de_inicio_quiz', str(datetime.now()))
                    return response
                else:
                    return render_template('tela_final.html')
            else:
                pergunta_atual += 1
                app.config['pergunta_atual'] = pergunta_atual
                if pergunta_atual < len(perguntas):
                    mensagem = f"Desculpe, a resposta correta era {respostas[pergunta_atual-1]}."
                    response = make_response(render_template('jogo_quiz.html', pergunta=perguntas[pergunta_atual], opcoes=opcoes[pergunta_atual], mensagem=mensagem))
                    response.set_cookie('pergunta_atual', str(pergunta_atual))
                    response.set_cookie('tempo_de_inicio_quiz', str(datetime.now()))
                    return response
                else:
                    return render_template('tela_final.html')
    else:
        # Se a página foi atualizada, voltar para a primeira pergunta
        pergunta_atual = 0
        app.config['pergunta_atual'] = pergunta_atual
        response = make_response(render_template('jogo_quiz.html', pergunta=perguntas[pergunta_atual], opcoes=opcoes[pergunta_atual], mensagem=''))
        response.set_cookie('pergunta_atual', str(pergunta_atual))
        response.set_cookie('tempo_de_inicio_quiz', str(datetime.now()))
        return response
    
@app.route('/inicial_quiz')
def Inicial_quiz():
    return render_template('inicial_quiz.html')

@app.route('/fases')
def Fases():
    return render_template('fases.html')

@app.route('/tempo_restante')
def Tempo_restante():
    tempo_de_inicio = request.cookies.get('tempo_de_inicio_quiz')
    if tempo_de_inicio is not None:
        tempo_de_inicio = datetime.strptime(tempo_de_inicio, '%Y-%m-%d %H:%M:%S.%f')
        tempo_restante = app.config['tempo_de_expiracao_quiz'] - (datetime.now() - tempo_de_inicio).total_seconds()
        if tempo_restante <= 0:
            tempo_restante = 0
        return jsonify({'tempo_restante_em_segundos': int(tempo_restante)})
    else:
        return jsonify({'tempo_restante_em_segundos': app.config['tempo_de_expiracao_quiz']})