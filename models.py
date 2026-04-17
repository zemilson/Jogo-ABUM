'''
Este módulo contém as funções para interagir com o banco de dados (operações CRUD).
'''
import database

# --- Funções para Membros ---

def add_membro(nome, endereco, telefone, email, data_nascimento, data_batismo, status='Ativo'):
    """Adiciona um novo membro ao banco de dados."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO membros (nome, endereco, telefone, email, data_nascimento, data_batismo, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, endereco, telefone, email, data_nascimento, data_batismo, status))
    conn.commit()
    conn.close()

def get_membros():
    """Retorna todos os membros do banco de dados."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM membros ORDER BY nome')
    membros = cursor.fetchall()
    conn.close()
    return membros

def update_membro(id, nome, endereco, telefone, email, data_nascimento, data_batismo, status):
    """Atualiza os dados de um membro."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE membros
    SET nome = ?, endereco = ?, telefone = ?, email = ?, data_nascimento = ?, data_batismo = ?, status = ?
    WHERE id = ?
    ''', (nome, endereco, telefone, email, data_nascimento, data_batismo, status, id))
    conn.commit()
    conn.close()

def delete_membro(id):
    """Deleta um membro do banco de dados."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM membros WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# --- Funções para Finanças ---

def add_transacao(tipo, categoria, valor, data, membro_id=None, descricao=''):
    """Adiciona uma nova transação financeira."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO financas (tipo, categoria, valor, data, membro_id, descricao)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (tipo, categoria, valor, data, membro_id, descricao))
    conn.commit()
    conn.close()

def get_transacoes():
    """Retorna todas as transações financeiras."""
    conn = database.connect_db()
    cursor = conn.cursor()
    # Junta com a tabela de membros para obter o nome
    cursor.execute('''
    SELECT f.id, f.tipo, f.categoria, f.valor, f.data, m.nome, f.descricao
    FROM financas f
    LEFT JOIN membros m ON f.membro_id = m.id
    ORDER BY f.data DESC
    ''')
    transacoes = cursor.fetchall()
    conn.close()
    return transacoes

def delete_transacao(id):
    """Deleta uma transação financeira."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM financas WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# --- Funções para Eventos ---

def add_evento(titulo, data, hora, local, descricao):
    """Adiciona um novo evento."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO eventos (titulo, data, hora, local, descricao)
    VALUES (?, ?, ?, ?, ?)
    ''', (titulo, data, hora, local, descricao))
    conn.commit()
    conn.close()

def get_eventos():
    """Retorna todos os eventos."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM eventos ORDER BY data DESC')
    eventos = cursor.fetchall()
    conn.close()
    return eventos

def delete_evento(id):
    """Deleta um evento."""
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM eventos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
