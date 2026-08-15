from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem-vindo"

@app.route("/curso")
def curso():
    return "Desenvolvimento de Sistemas"

@app.route("/escola")
def escola():
    return "CEEP Cascavel"

if __name__ == "__main__":
    app.run(debug=True)
