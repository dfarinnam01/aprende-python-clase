from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

entradas = []
contador_entradas=0
@app.route("/")
def inicio():
    return "Ejercicio 4"

@app.route("/api/entradas",methods=["POST"])
def nueva():
    global contador_entradas
    data = request.get_json()
    num_entrada = data.get("num_entrada","")
    dni = data.get("dni", "")

    if not num_entrada:
        data={"msg":"Número de entrada no indicado"}
        return jsonify(data),404

    if not dni:
        return jsonify({"msg": "DNI no indicado"}), 404

    for entrada in entradas:
        if entrada["num_entrada"] == num_entrada:
            return jsonify({"msg": f"La entrada {num_entrada} ya existe"}), 404

    contador_entradas += 1
    entradas.append({
        "id": contador_entradas,
        "num_entrada": num_entrada,
        "dni": dni
    })

    data={"posicion": len(entradas)-1, "msg": f"La entrada {num_entrada} ha sido añadida"}
    return jsonify(data)

@app.route("/api/entradas")
def listado_entradas():
    return jsonify(entradas)

@app.route("/api/entradas/<int:id_entrada>",methods=["GET"])
def get(id_entrada):
    for entrada in entradas:
        if entrada["id"] == id_entrada:
            return jsonify({"entrada":entrada,"msg": f"La entrada {id_entrada} encontrada"}), 404
    return jsonify({
        "msg": f"La entrada {id_entrada} no existe"
    }), 404

@app.route("/api/entradas/<int:id_entrada>",methods=["DELETE"])
def borrar(id_entrada):
    for entrada in entradas:
        if entrada["id"] == id_entrada:
            entradas.remove(entrada)
            return jsonify({
                "msg": f"La entrada {id_entrada} ha sido eliminada"
            })
    return jsonify({
        "msg": f"La entrada {id_entrada} no existe"
    }), 404

@app.route("/api/entradas/<int:id_entrada>",methods=["PUT"])
def modificar(id_entrada):
    data = request.get_json()
    num_entrada = data.get("num_entrada", None)
    dni = data.get("dni", None)

    if not num_entrada:
        data = {"msg": "Número de entrada no indicado"}
        return jsonify(data), 404
    if not dni:
        return jsonify({"msg": "DNI no indicado"}), 404

    for entrada in entradas:
        if entrada["id"] == id_entrada:
            entrada["num_entrada"] = num_entrada
            entrada["dni"] = dni
            return jsonify({
                "msg": f"La entrada {id_entrada} ha sido modificada",
                "entrada": entrada
            })

        return jsonify({
            "msg": f"La entrada {id_entrada} no existe"
        }), 404

@app.route("/saludo1")
def saludo1():
    return ("<html><body><p>Saludos <b>D.Pepito</p></body></html>"
            "")

@app.route("/saludo2/<nombre>")
def saludo2(nombre):
    return render_template("saludos.html", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)