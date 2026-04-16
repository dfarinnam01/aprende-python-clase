from flask import Flask, jsonify, render_template

app = Flask(__name__)

entradas= []
@app.route("/")
def inicio():
    return "Ejercicio 2"

@app.route("/api/entradas/nueva/<string:num_entrada>")
def nueva(num_entrada):
    if num_entrada in entradas:
        data={"msg": f"La entrada {num_entrada} ya existe"}
        return jsonify(data), 400

    entradas.append(num_entrada)
    data={"posicion": len(entradas)-1, "msg": f"La entrada {num_entrada} ha sido añadida"}
    return jsonify(data)

@app.route("/api/entradas")
def listado_entradas():
    return jsonify(entradas)

@app.route("/api/entradas/<int:id_entrada>")
def consulta(id_entrada):
    if id_entrada >= len(entradas):
        data={"msg": f"La entrada {id_entrada} no existe"}
        return jsonify(data),400
    data={"entrada": entradas[id_entrada],
          "msg": f"La entrada {id_entrada} es {entradas[id_entrada]}"}
    return jsonify(data)
@app.route("/saludo1")
def saludo1():
    return ("<html><body><p>Saludos <b>D.Pepito</p></body></html>"
            "")

@app.route("/saludo2/<nombre>")
def saludo2(nombre):
    return render_template("saludos.html", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)