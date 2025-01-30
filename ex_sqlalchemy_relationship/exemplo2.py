from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import Table, Column, ForeignKey
from typing import List

engine = create_engine('sqlite:///exemplo2.db')

session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

# Relacionamento  1 x N  /  # back populates - faz referncia a varivel oposta do relacionamneto, 

class Estudante(Base):
    __tablename__ = 'students'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    curso_id: Mapped[int] = mapped_column(ForeignKey('courses.id'), nullable='True') # constitui na tabela o relacinamneto

    def __repr__(self) -> str:
        return f"Estudante={self.nome}"


class Curso(Base):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    #back_populates - define nas duas classes
    estudantes:Mapped[List['Estudante']] = relationship('Estudante', backref='curso') # utilizar o relacionamento em nivel de orientaçao obejto
    # que já exite para buscar uma lista de studantes que pertemcem ao curso no nivel da aplicação

    def __repr__(self) -> str:
        return f"Curso={self.nome}"

Base.metadata.create_all(bind=engine)

#info = Curso(nome='Informática')
#x = Estudante(nome='Batista', curso_id=1)
#y = Estudante(nome='Chico', curso_id=1)
#z = Estudante(nome = 'Mané Cabelim')

#session.add(info)
#ession.add_all([x,y,z])
#session.commit()

# select * from tb_curso where id = 1
curso = session.query(Curso).get(1)
print(curso)

estudante = session.query(Estudante).get(1)
print(estudante.curso)

print(str(estudante) + " estuda " + str(estudante.curso))