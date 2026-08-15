from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("produtos.db")
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabela():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL
        )
    """)

    conexao.commit()
    conexao.close()

@app.route("/produtos", methods=["GET"])
def listar():
    conexao = conectar()

    cursor = conexao.execute("SELECT * FROM produtos")

    produtos = [dict(p) for p in cursor.fetchall()]

    conexao.close()

    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def criar():
    novo = request.get_json()

    conexao = conectar()

    cursor = conexao.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
        (novo["nome"], novo.get("preco"))
    )

    conexao.commit()

    novo_id = cursor.lastrowid

    conexao.close()

    return jsonify({
        "id": novo_id,
        **novo
    }), 201

@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()

    conexao = conectar()

    cursor = conexao.execute(
        "UPDATE produtos SET nome = ?, preco = ? WHERE id = ?",
        (dados["nome"], dados.get("preco"), id)
    )

    conexao.commit()

    afetadas = cursor.rowcount

    conexao.close()

    if afetadas == 0:
        return jsonify({
            "erro": "Produto nao encontrado"
        }), 404

    return jsonify({
        "id": id,
        **dados
    })

criar_tabela()

if __name__ == "__main__":
    app.run(debug=True)
