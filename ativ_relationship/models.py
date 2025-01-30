from database import db

from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List, Optional
from sqlalchemy import Table, Column, ForeignKey


class Locadora(db.Model):
    __tablename__ = "locadora_tabela"
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente_tabela.id"), primary_key=True)
    veiculo_id: Mapped[int] = mapped_column(ForeignKey("veiculo_tabela.id"), primary_key=True)
    data: Mapped[Optional[str]]

    veiculo: Mapped["Veiculos"] = relationship(back_populates='clientes_locadora')
    cliente: Mapped["Clientes"] = relationship(back_populates='veiculo_locadora')

class Clientes(db.Model):
    __tablename__ = 'cliente_tabela'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    veiculos: Mapped[List['Veiculos']] = relationship(secondary='locadora_tabela',back_populates='clientes') # lista de cursos qur o estudante tem

    veiculo_locadora: Mapped[List["Locadora"]] = relationship(back_populates="cliente")

    def __repr__(self) -> str:
        return f"Cliente={self.nome}"


class Veiculos(db.Model):
    __tablename__ = 'veiculo_tabela'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]

    clientes: Mapped[List["Clientes"]] = relationship(secondary='locadora_tabela', back_populates='veiculos')
    clientes_locadora: Mapped[List['Locadora']] = relationship(back_populates='veiculo') # lista de cursos qur o estudante tem

    def __repr__(self) -> str:
        return f"Veiculo={self.nome}"

