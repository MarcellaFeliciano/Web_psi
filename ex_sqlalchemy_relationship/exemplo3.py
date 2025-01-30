from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

engine = create_engine('sqlite:///exemplo3.db')

session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

# AUTO RELACIONAMENTO
class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    gerente_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    # gerenciados: Mapped[List['User']] = relationship('User', back_populates='gerente')
    gerenciados = relationship('User', back_populates='gerente')  # back populates - faz referncia a varivel oposta do relacionamneto, 
    gerente = relationship('User', back_populates='gerenciados', remote_side=[id]) # o lado remoto para char o gerente, considera a propria tabela / como tabelaa remoda , na coluna id 

    def __repr__(self) -> str:
        return self.nome

Base.metadata.create_all(bind=engine) # craição do mapeamneto usando a engine que sqlalchemy tem, 

"""

user1 = User(nome='Hugo')
session.add(user1)
session.commit()

#quem é gerenciado tem o id do gerente (hugo é gerente = id 1)
user2 = User(nome='Romerito', gerente_id=1)
user3 = User(nome='Iuri', gerente_id=1)
user4 = User(nome='Daniel')

session.add_all([user2,user3,user4])
session.commit()"""

sql = select(User).where(User.id == 1)
chefe = session.execute(sql).scalars().first()
print(chefe.nome)

print(chefe.gerenciados) # lista de pessoas relacionados ao gerente (pessoas gerenciadas pelo id 1)

sql = select(User).where(User.id == 3)
pessoa = session.execute(sql).scalars().first()
print("Eu sou " + pessoa.nome)
print("Meu chefe é " + str(pessoa.gerente))