""" 

# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#setting-bi-directional-many-to-many



class Association(Base):
    __tablename__ = "association_table"

    left_id: Mapped[int] = mapped_column(ForeignKey("left_table.id"), primary_key=True)
    right_id: Mapped[int] = mapped_column(
        ForeignKey("right_table.id"), primary_key=True
    )
    extra_data: Mapped[Optional[str]]

    # association between Assocation -> Child
    child: Mapped["Child"] = relationship(back_populates="parent_associations")

    # association between Assocation -> Parent
    parent: Mapped["Parent"] = relationship(back_populates="child_associations")


class Parent(Base):
    __tablename__ = "left_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    # many-to-many relationship to Child, bypassing the `Association` class
    children: Mapped[List["Child"]] = relationship(
        secondary="association_table", back_populates="parents"
    )

    # association between Parent -> Association -> Child
    child_associations: Mapped[List["Association"]] = relationship(
        back_populates="parent"
    )


class Child(Base):
    __tablename__ = "right_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    # many-to-many relationship to Parent, bypassing the `Association` class
    parents: Mapped[List["Parent"]] = relationship(
        secondary="association_table", back_populates="children"
    )

    # association between Child -> Association -> Parent
    parent_associations: Mapped[List["Association"]] = relationship(
        back_populates="child"
    )
    """



  # código não funcional!!

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from typing import List
from sqlalchemy import Table, Column, ForeignKey

engine = create_engine('sqlite:///exemplo4.db')

session = Session(bind=engine)

class Base(DeclarativeBase):
    pass



class Consulta(Base):
    __tablename__ = "consulta"
    medico_id: Mapped[int] = mapped_column(ForeignKey("medico_tabela.id"), primary_key=True)
    paciente_id: Mapped[int] = mapped_column(ForeignKey("paciente_tabela.id"), primary_key=True)
    data: Mapped[str]

    paciente: Mapped['Paciente'] = relationship(back_populates='medicos')
    medico: Mapped['Medico'] = relationship(back_populates='pacientes')
    
class Medico(Base):
    __tablename__ = 'medico_tabela'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    pacientes: Mapped[List['Consulta']] = relationship(back_populates='medico') # lista de cursos qur o estudante tem


class Paciente(Base):
    __tablename__ = 'paciente_tabela'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    medicos = Mapped[List['Consulta']] = relationship(back_populates='paciente') # lista de cursos qur o estudante tem

Base.metadata.create_all(bind=engine)


m1 = Medico(nome='Marcella')
p1 = Paciente(nome='Batista')
p2 = Paciente(nome='Chico')

session.add(m1)
session.add_all([p1,p2])
session.commit()

info = session.query(Medico).get(1) # o curso 1 = informatica
print(info)
