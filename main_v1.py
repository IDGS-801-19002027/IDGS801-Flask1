# Archivo principal de trabajo y estructura inicial de Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo Flask cambios nuevos"

if __name__ == "__main__":
    app.run(debug = True, port = 3000)