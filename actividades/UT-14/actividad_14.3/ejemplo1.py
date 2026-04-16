from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola mundo con Flask"

@app.route("/saludo")
def saludo():
    return "¡Hola!"

if __name__ == "__main__":
    app.run(deug=True)