from sqlite3 import IntegrityError

from flask import Flask, jsonify, render_template, request

from db import db, init_db
from models import Entrada
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

init_db(app)

with app.app_context():
    db.create_all()

@app.route("/")
def inicio():
    return "Ejercicio 4"

@app.route("/api/entradas",methods=["POST"])
def nueva():

    data = request.get_json()
    num_entrada = data.get("num_entrada","")
    dni = data.get("dni", "")

    if not num_entrada:
        data={"msg":"Número de entrada no indicado"}
        return jsonify(data),404

    if not dni:
        return jsonify({"msg": "DNI no indicado"}), 404

    entrada = Entrada.query.filter_by(num_entrada=num_entrada).first()

    if entrada:
      data={"msg":f"La entrada {num_entrada} ya existe"}
      return jsonify(data),400

    entrada = Entrada(num_entrada=num_entrada,dni=dni)
    db.session.add(entrada)
    try:
        db.session.commit()
        data = {"entrada": entrada.to_dict(), "msg": f"La entrada {num_entrada} ha sido añadida"}
        return jsonify(data),201
    except Exception as e:
        db.session.rollback()
        logger.error(f"No se pudo añadir la entrada: {data}: {e}")
        data={"msg":f"No se pudo añadir la entrada: {data}"}
        return jsonify(data),400

@app.route("/api/entradas")
def listado_entradas():
    row=Entrada.query.all()
    entradas = [e.to_dict() for e in row]
    return jsonify(entradas)

@app.route("/api/entradas/<int:id_entrada>",methods=["GET"])
def get(id_entrada):
    entrada = Entrada.query.get(id_entrada)
    if not entrada:
        data={"msg":f"La entrada de id {id_entrada} no existe"}
        return jsonify(data),404
    data = {"entrada": entrada.to_dict(), "msg":f"En numero de entrada asociado al id{id_entrada} es {entrada.num_entrada}"}
    return jsonify(data)

@app.route("/api/entradas/<int:id_entrada>",methods=["DELETE"])
def borrar(id_entrada):
    data = request.get_json()
    entrada = Entrada.query.get(id_entrada)
    if not entrada:
        data = {"msg": f"La entrada de id {id_entrada} no existe"}
        return jsonify(data), 404
    try:
        db.session.delete(entrada)
        db.session.commit()
        data = {"entrada":entrada.to_dict(),"msg": f"La entrada de id {id_entrada} ha sido borrada"}
        return jsonify(data),200
    except Exception as e:
        db.session.rollback()
        data = {"msg": f"No se pudo borrar la entrada con id {id_entrada}"}
        return jsonify(data),400

@app.route("/api/entradas/<int:id_entrada>",methods=["PUT"])
def modificar(id_entrada):
    data = request.get_json()
    entrada = Entrada.query.get(id_entrada)
    num_entrada = data.get("num_entrada", None)
    dni = data.get("dni", None)

    if not num_entrada:
        data = {"msg": "Número de entrada no indicado"}
        return jsonify(data), 400

    entrada.num_entrada = num_entrada
    entrada.dni = dni

    try:
        db.session.commit()
        data={"entrada":entrada.to_dict(),"msg":f"Entrada con id {id_entrada} ha sido modificada"}
        return jsonify(data)
    except Exception as e:
        db.session.rollback()
        logger.error(f"No se pudo actualizar la entrada: {data}: {e}")
        data = {"msg": f"No se pudo actualizar la entrada: {data}"}
        return jsonify(data),400

@app.route("/saludo1")
def saludo1():
    return ("<html><body><p>Saludos <b>D.Pepito</p></body></html>"
            "")

@app.route("/saludo2/<nombre>")
def saludo2(nombre):
    return render_template("saludos.html", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)