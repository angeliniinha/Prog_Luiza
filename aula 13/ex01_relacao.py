import sqlite3

def conectar():
    conexao = sqlite3.connect("biblioteca.db")
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabelas():
    conexao = conectar()

    conexao.execute("""
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    conexao.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES autores(id)
    )
    """)

    conexao.commit()
    conexao.close()

def inserir_dados():
    conexao = conectar()

    conexao.execute(
        "INSERT INTO autores (nome) VALUES (?)",
        ("Machado de Assis",)
    )

    conexao.execute(
        "INSERT INTO autores (nome) VALUES (?)",
        ("George Orwell",)
    )

    conexao.execute(
        "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
        ("Dom Casmurro", 1)
    )

    conexao.execute(
        "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
        ("Memórias Póstumas de Brás Cubas", 1)
    )

    conexao.execute(
        "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
        ("1984", 2)
    )

    conexao.commit()
    conexao.close()

criar_tabelas()
inserir_dados()

print("Banco criado e dados inseridos com sucesso!")
