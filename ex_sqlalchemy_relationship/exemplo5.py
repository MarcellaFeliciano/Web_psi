
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from typing import List, Optional
from sqlalchemy import Table, Column, ForeignKey

engine = create_engine('sqlite:///exemplo123.db')

session = Session(bind=engine)

class Base(DeclarativeBase):
    pass



class Consulta(Base):
    __tablename__ = "consulta_tabela"
    # talves adicionar um id para a tabela secundaria
    medico_id: Mapped[int] = mapped_column(ForeignKey("medico_tabela.id"), primary_key=True)
    paciente_id: Mapped[int] = mapped_column(ForeignKey("paciente_tabela.id"), primary_key=True)
    data: Mapped[Optional[str]]

    paciente: Mapped["Paciente"] = relationship(back_populates='medico_consulta')
    medico: Mapped["Medico"] = relationship(back_populates='paciente_consulta')
    
class Medico(Base):
    __tablename__ = 'medico_tabela'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    pacientes: Mapped[List['Paciente']] = relationship(secondary='consulta_tabela',back_populates='medicos') # lista de cursos qur o estudante tem

    paciente_consulta: Mapped[List["Consulta"]] = relationship(back_populates="medico")

    def __repr__(self) -> str:
        return f"Medico={self.nome}"


class Paciente(Base):
    __tablename__ = 'paciente_tabela'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]

    medicos: Mapped[List["Medico"]] = relationship(secondary='consulta_tabela', back_populates='pacientes')
    medico_consulta: Mapped[List['Consulta']] = relationship(back_populates='paciente') # lista de cursos qur o estudante tem

    def __repr__(self) -> str:
        return f"Paciente={self.nome}"

Base.metadata.create_all(bind=engine)

clientes = session.query(Paciente).all()
print(clientes)
for cliente in clientes:
    print(cliente.nome)

"""
m1 = Medico(nome='Cecilia')
m2 = Medico(nome='Evelyn')
p1 = Paciente(nome='Paulo')
p2 = Paciente(nome='Maria')

session.add(m1)
session.add(m2)
session.add_all([p1,p2])
session.commit()

info = session.query(Medico).get(1) # o curso 1 = informatica
print(info)



p3 = Paciente(nome='Julia')

info = session.query(Medico).get(1) # o curso 1 = informatica
print(info)
info.pacientes.append(p3)
session.commit()
p1 = session.query(Paciente).get(1)
info = session.query(Medico).get(1)
info.pacientes.append(p1)
session.commit()

p1 = session.query(Paciente).get(1)
info = session.query(Medico).get(1)
info.pacientes.append(p1)
session.commit()

p1 = session.query(Paciente).get(2)
print(p1.nome)

con = Consulta(medico_id='1', paciente_id='2', data='2025-01-29')
session.add(con)
session.commit()
print(con.data)


con = Consulta(medico_id='2', paciente_id='1', data='2025-01-29')
session.add(con)
session.commit()


info = session.query(Medico).get(2)
print(info.paciente_consulta[0].medico)

con = session.query(Consulta).first()
con.data = '2025-01-20'
session.commit()
print(con)


#info.pacientes.append(p1) # vinculação da variavel estudantes ao curso 1 o aluno 1 
#session.commit()

#info.pacientes.remove(p1)
#session.commit()
"""