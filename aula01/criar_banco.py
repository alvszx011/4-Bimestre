import sqlite3

conn = sqlite3.connect('escola.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos(
        id      INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome    TEXT NOT NULL,
        nota1   REAL,
        nota2   REAL,
        nota3   REAL,
        situacao TEXT              
)
""")

conn.commit()
conn.close()
print('Tabela criada.')

