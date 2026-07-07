from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():
    return "Bem-vindo à minha primeira API com Flask!"

@app.route("/data")
def data():
    hoje = date.today()
    return f"Data de hoje: {hoje}"

if __name__ == "__main__":
    app.run(debug=True)
