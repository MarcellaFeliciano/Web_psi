
CREATE TABLE tb_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);


CREATE TABLE tb_livros (
    liv_id INTEGER PRIMARY KEY AUTOINCREMENT,
    liv_titulo TEXT NOT NULL,
    liv_categoria TEXT NOT NULL,

);