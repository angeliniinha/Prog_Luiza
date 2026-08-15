from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {
        "id": 1,
        "nome": "Pizza Calabresa",
        "preco": 45.00,
        "disponivel": True
    },
    {
        "id": 2,
        "nome": "Pizza Frango",
        "preco": 48.00,
        "disponivel": True
    },
    {
        "id": 3,
        "nome": "Pizza Portuguesa",
        "preco": 50.00,
        "disponivel": False
    },
    {
        "id": 4,
        "nome": "Pizza Marguerita",
        "preco": 42.00,
        "disponivel": True
    }
]

@app.route("/produtos/<int:id>")
def buscar_produto(id):

    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)

    return jsonify({"erro": "Produto nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
