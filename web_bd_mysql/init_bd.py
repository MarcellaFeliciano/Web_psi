from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'marcella123'
app.config['MYSQL_DB'] = 'mysql'  # Use o banco de dados padrão para executar o SQL
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

conn = MySQL(app)

def iniciar_banco_dados(filename):
    with app.app_context():  #Criando o contexto da aplicação
        cursor = conn.connection.cursor()
        with open(filename, 'r') as file:
            mysql = file.read() #Lê o arquivo e armazena como uma string
            comandos_raw = mysql.split(';') #Divide o conteúdo do arquivo em uma lista usando ';' como delimitador

            commands = [] #Lista para armazenar comandos SQL limpos
            for comando in comandos_raw:
                comando_limpo = comando.strip() #Remover espaços em branco no início e no fim do comando
                if comando_limpo:#Verificar se o comando não está vazio
                    commands.append(comando_limpo)#Adicionar o comando limpo à lista 'commands'

            for command in commands: #percorrendo os comandos limpos
                cursor.execute(command) #executando cada comando
        conn.connection.commit()
        cursor.close()

if __name__ == "__main__":
    iniciar_banco_dados('db/schema.sql') 
    print("Banco de dados inicializado com sucesso!")
