

"""

from dotenv import load_dotenv
import os
import smtplib # enviar emails usando o smtp

load_dotenv()

# print(os.getenv('SENDER')) # pegar o dado do sender em env

message = f"""\
#subjetc: hi
#To: {os.getenv('SENDER')}
F#rom: {os.getenv('SENDER')}

#This is a test. 
"""

with smtplib.smtp(os.getenv('SERVER'), os.getenv('PORT')) as server:  # cdriando uma estancia para ter acesso mpara enviar os emails
    server.startls() # segurança - criptografar as menssagens
    user = os.getenv("sender")
    senha = os.getenv('password')
    server.login(user, senha)
    server.sendmail(sender, user, message)


    """




    from flask import flask
    from flask_mail import mail
    import os
    from dotenv import load_dotenv


    load_dotenv()
    mail = Mail()
    app  Flask(__name__)

    app.config['MAILO_SERVER']

    mail.init_app(app)

    @app.route("/")
    def send()
    pass