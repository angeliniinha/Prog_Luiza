from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado", "preco": 80.00}
]

@app.route("/produtos", methods=["GET"])
def listar():
    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def criar():
    novo = request.get_json()

    produtos.append(novo)

    return jsonify(novo), 201

if __name__ == "__main__":
    app.run(debug=True)
