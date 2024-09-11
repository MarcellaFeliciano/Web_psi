import sqlite3

database = "database.db"
conn = sqlite3.connect(database)

SCHEMA = "database/schema.sql"
with open(SCHEMA) as f:
    conn.executescript(f.read())


# encerra operações
conn.commit()
conn.close()