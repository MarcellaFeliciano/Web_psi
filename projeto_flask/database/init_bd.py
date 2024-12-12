import sqlite3

# abre conexão
conn = sqlite3.connect('database/database.db')

# localização do sql
SCHEMA = "database/schema.sql"

# executa declarações do sql para o banco
with open(SCHEMA) as f:
    conn.executescript(f.read())
    
# encerra operações
conn.commit()
conn.close()