import sqlite3

# Conectar ao banco de dados (ou criar um novo se não existir)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Criar a tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    Local TEXT PRIMARY KEY,
    Valor TEXT NOT NULL,
    Pago TEXT NOT NULL,
    Serie TEXT NOT NULL,
    Data1 TEXT NOT NULL,
    Data2 TEXT NOT NULL,
    Data3 TEXT NOT NULL
)
''')

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()
