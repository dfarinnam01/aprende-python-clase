from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Hola mundo con Flask"


@app.route("/saludo")
def saludo():
    return "¡Hola!"

@app.route("/info")
def info():
    info = { "siglas": "CEPY", "descripcion": "C.E. Desarrollo de aplicaciones en lenguaje Python "}
    return info,400
@app.route("/ficha-cepy")
def ficha_cepy():
    return send_file("ficha-cepy.pdf")

if __name__ == "__main__":
    app.run(debug=True)


