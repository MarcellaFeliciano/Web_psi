CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_user_id TEXT NOT NULL,
    emp_book_id TEXT NOT NULL,
    emp_data TEXT NOT NULL,
    FOREIGN KEY(emp_user_id) REFERENCES users(id),
    FOREIGN KEY(emp_book_id) REFERENCES books(id)
);