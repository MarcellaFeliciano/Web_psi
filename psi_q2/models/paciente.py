
from database import get_connection

class Paciente:
    def __init__(self, nome: str, genero: str, idade: int, telefone: str):
        self.nome = nome
        self.genero = genero
        self.idade = idade
        self.telefone = telefone
        

    def registrar(self):
        conn = get_connection()
        conn.execute("INSERT INTO tb_pacientes(nome_completo, genero, idade, telefone) values(?,?,?,?)", (self.nome, self.genero, self.idade, self.telefone))
        conn.commit()
        conn.close()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        pacientes = conn.execute("SELECT * FROM tb_pacientes").fetchall()
        return pacientes
