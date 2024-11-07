from database import get_connection

class Medico:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha


    @classmethod
    def all(cls):
        conn = get_connection()
        medicos = conn.execute("SELECT * FROM tb_medicos").fetchall()
        return medicos


    def cadastrar(self):
        conn = get_connection()
        conn.execute("INSERT INTO tb_medicos(nome, email, senha) values(?,?,?)", (self.nome, self.email, self.senha))
        conn.commit()
        conn.close()
        return True

    def logar(self):
        conn = get_connection()
        user = conn.execute("SELECT * FROM tb_medicos WHERE email = ?", (self.email,)).fetchone()
        
        if user is not None:
            if user['email'] == self.email and user['senha'] == self.senha: 
                self.nome = user['nome']
                return True
            else:
                return False
        else:
            return False
       
    
        