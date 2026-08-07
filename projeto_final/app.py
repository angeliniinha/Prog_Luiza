from flask import Flask, request, jsonify
from database import conectar, criar_tabelas

app = Flask(__name__)

# Criar banco e tabelas ao iniciar
criar_tabelas()

@app.route("/categorias", methods=["GET"])
def listar_categorias():
    conn = conectar()
    categorias = conn.execute(
        "SELECT * FROM categorias"
    ).fetchall()
    conn.close()

    return jsonify([dict(c) for c in categorias]), 200

@app.route("/categorias/<int:id>", methods=["GET"])
def buscar_categoria(id):
    conn = conectar()

    categoria = conn.execute(
        "SELECT * FROM categorias WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    if categoria is None:
        return jsonify({"erro": "Categoria não encontrada"}), 404

    return jsonify(dict(categoria)), 200

@app.route("/categorias", methods=["POST"])
def criar_categoria():
    dados = request.json

    if not dados or "nome" not in dados:
        return jsonify({"erro": "Nome obrigatório"}), 400

    conn = conectar()

    cursor = conn.execute(
        "INSERT INTO categorias (nome) VALUES (?)",
        (dados["nome"],)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "id": cursor.lastrowid,
        "nome": dados["nome"]
    }), 201

@app.route("/categorias/<int:id>", methods=["PUT"])
def atualizar_categoria(id):
    dados = request.json

    if not dados or "nome" not in dados:
        return jsonify({"erro": "Nome obrigatório"}), 400

    conn = conectar()

    categoria = conn.execute(
        "SELECT * FROM categorias WHERE id = ?",
        (id,)
    ).fetchone()

    if categoria is None:
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    conn.execute(
        "UPDATE categorias SET nome = ? WHERE id = ?",
        (dados["nome"], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Categoria atualizada"}), 200

@app.route("/categorias/<int:id>", methods=["DELETE"])
def excluir_categoria(id):
    conn = conectar()

    categoria = conn.execute(
        "SELECT * FROM categorias WHERE id = ?",
        (id,)
    ).fetchone()

    if categoria is None:
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    conn.execute(
        "DELETE FROM categorias WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Categoria removida"}), 200

@app.route("/pizzas", methods=["GET"])
def listar_pizzas():
    conn = conectar()

    pizzas = conn.execute(
        "SELECT * FROM pizzas"
    ).fetchall()

    conn.close()

    return jsonify([dict(p) for p in pizzas]), 200

@app.route("/pizzas/<int:id>", methods=["GET"])
def buscar_pizza(id):
    conn = conectar()

    pizza = conn.execute(
        "SELECT * FROM pizzas WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    if pizza is None:
        return jsonify({"erro": "Pizza não encontrada"}), 404

    return jsonify(dict(pizza)), 200

@app.route("/pizzas", methods=["POST"])
def criar_pizza():
    dados = request.json

    campos = ["nome", "preco", "categoria_id"]

    if not dados or not all(campo in dados for campo in campos):
        return jsonify({"erro": "Dados obrigatórios faltando"}), 400

    conn = conectar()

    categoria = conn.execute(
        "SELECT * FROM categorias WHERE id = ?",
        (dados["categoria_id"],)
    ).fetchone()

    if categoria is None:
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    cursor = conn.execute(
        """
        INSERT INTO pizzas
        (nome, preco, categoria_id)
        VALUES (?, ?, ?)
        """,
        (
            dados["nome"],
            dados["preco"],
            dados["categoria_id"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "id": cursor.lastrowid,
        "nome": dados["nome"],
        "preco": dados["preco"],
        "categoria_id": dados["categoria_id"]
    }), 201

@app.route("/pizzas/<int:id>", methods=["PUT"])
def atualizar_pizza(id):
    dados = request.json

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    conn = conectar()

    pizza = conn.execute(
        "SELECT * FROM pizzas WHERE id = ?",
        (id,)
    ).fetchone()

    if pizza is None:
        conn.close()
        return jsonify({"erro": "Pizza não encontrada"}), 404

    conn.execute(
        """
        UPDATE pizzas
        SET nome = ?, preco = ?, categoria_id = ?
        WHERE id = ?
        """,
        (
            dados["nome"],
            dados["preco"],
            dados["categoria_id"],
            id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Pizza atualizada"}), 200

@app.route("/pizzas/<int:id>", methods=["DELETE"])
def excluir_pizza(id):
    conn = conectar()

    pizza = conn.execute(
        "SELECT * FROM pizzas WHERE id = ?",
        (id,)
    ).fetchone()

    if pizza is None:
        conn.close()
        return jsonify({"erro": "Pizza não encontrada"}), 404

    conn.execute(
        "DELETE FROM pizzas WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Pizza removida"}), 200

@app.route("/pizzas/detalhes", methods=["GET"])
def pizzas_detalhes():

    conn = conectar()

    pizzas = conn.execute(
        """
        SELECT
            pizzas.id,
            pizzas.nome AS pizza,
            pizzas.preco,
            categorias.nome AS categoria
        FROM pizzas
        INNER JOIN categorias
        ON pizzas.categoria_id = categorias.id
        """
    ).fetchall()

    conn.close()

    return jsonify([dict(p) for p in pizzas]), 200

@app.route("/categorias/<int:id>/pizzas", methods=["GET"])
def pizzas_categoria(id):

    conn = conectar()

    pizzas = conn.execute(
        """
        SELECT *
        FROM pizzas
        WHERE categoria_id = ?
        """,
        (id,)
    ).fetchall()

    conn.close()

    return jsonify([dict(p) for p in pizzas]), 200

@app.route("/pizzas/busca", methods=["GET"])
def buscar_nome():

    nome = request.args.get("nome")

    if not nome:
        return jsonify({"erro": "Informe um nome"}), 400

    conn = conectar()

    pizzas = conn.execute(
        """
        SELECT *
        FROM pizzas
        WHERE nome LIKE ?
        """,
        ("%" + nome + "%",)
    ).fetchall()

    conn.close()

    return jsonify([dict(p) for p in pizzas]), 200

if __name__ == "__main__":
    app.run(debug=True)
