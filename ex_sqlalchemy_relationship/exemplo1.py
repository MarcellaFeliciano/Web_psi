from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from typing import List
from sqlalchemy import Table, Column, ForeignKey

engine = create_engine('sqlite:///exemplo1.db')

session = Session(bind=engine)

class Base(DeclarativeBase):
    pass


# relacionamento NxN

# tabela intermediaria entre os estudantes eos cirsos, pois o aluno pode pertencer a varios cursos
# a criação de chaves estrangeiras/primarias para relacionar varias vezes o mesmo aluno ao curso
students_courses = Table(
    'students_courses',
    Base.metadata,
    Column('students_id', ForeignKey('students.id'), primary_key=True),
    Column('courses_id', ForeignKey('courses.id'), primary_key=True)
)

class Estudante(Base):
    __tablename__ = 'students'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    cursos: Mapped[List['Curso']] = relationship('Curso', secondary=students_courses, back_populates='estudantes') # lista de cursos qur o estudante tem


class Curso(Base):
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    estudantes = relationship('Estudante', secondary=students_courses, back_populates='cursos') # lista os alunos vinculados ao curso

Base.metadata.create_all(bind=engine)

info = Curso(nome='Informática')
x = Estudante(nome='Batista')
y = Estudante(nome='Chico')
z = Estudante(nome = 'Mané Cabelim')

session.add(info)
session.add_all([x,y,z])
session.commit()


info = session.query(Curso).get(1) # o curso 1 = informatica
info.estudantes.append(x) # vinculação da variavel estudantes ao curso 1 o aluno 1 
session.commit()

info.estudantes.remove(x)
session.commit()
