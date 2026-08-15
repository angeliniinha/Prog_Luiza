import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL
)
""")

cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
    ("Teclado", 80.00)
)

cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
    ("Mouse", 50.00)
)

cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
    ("Monitor", 700.00)
)

conexao.commit()
conexao.close()

print("Produtos inseridos com sucesso!")
