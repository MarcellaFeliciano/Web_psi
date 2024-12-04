from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

from app import db
conn = db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]

    def all():
        users = conn.session.execute(conn.select(User)).scalars()
        return users

    def get_user(id):
        user = User.query.get_or_404(id)  
        return user


    def add_user(email,senha):
        user = User(email=email,senha=senha,)
        conn.session.add(user)
        conn.session.commit()

            
    def edit_email(id,email):
        user = User.get_user(id)
        user.email = email
        conn.session.commit() 


