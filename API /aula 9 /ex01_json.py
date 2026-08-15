from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produto")
def produto():
    dados = {
        "id": 1,
        "nome": "Pizza Calabresa",
        "preco": 45.00,
        "disponivel": True
    }
