'''
Este módulo é responsável pela criação e conexão com o banco de dados SQLite.
'''
import sqlite3

def connect_db():
    """Conecta ao banco de dados e retorna a conexão."""
    return sqlite3.connect('igreja.db')

def create_tables():
    """Cria as tabelas do banco de dados se elas não existirem."""
    conn = connect_db()
    cursor = conn.cursor()

    # Tabela de Membros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS membros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT,
        telefone TEXT,
        email TEXT,
        data_nascimento TEXT,
        data_batismo TEXT,
        status TEXT DEFAULT 'Ativo'
    )
    ''')

    # Tabela de Finanças (Dízimos e Ofertas)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS financas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL, -- 'Entrada' ou 'Saída'
        categoria TEXT, -- 'Dízimo', 'Oferta', 'Despesa Administrativa', etc.
        valor REAL NOT NULL,
        data TEXT NOT NULL,
        membro_id INTEGER,
        descricao TEXT,
        FOREIGN KEY (membro_id) REFERENCES membros (id)
    )
    ''')

    # Tabela de Eventos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        data TEXT NOT NULL,
        hora TEXT,
        local TEXT,
        descricao TEXT
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Banco de dados e tabelas criados com sucesso!")
