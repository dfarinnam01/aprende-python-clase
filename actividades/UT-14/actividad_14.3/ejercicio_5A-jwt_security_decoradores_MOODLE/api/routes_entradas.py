# routes/entradas.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
import logging


from db import db
from models import Entrada
from decorators import roles_required, require_json


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


entradas_bp = Blueprint("entradas", __name__)

# =========================
# CREATE ENTRADA (ADMIN)
# =========================
@entradas_bp.route("", methods=["POST"])
@require_json
@jwt_required()
@roles_required("ADMIN")
def create():
    user = get_jwt_identity()
    claims = get_jwt()
    logger.info(user)
    logger.info(claims)

    payload  = request.get_json()

    num_entrada = payload.get("num_entrada")
    dni = payload.get("dni")

    if not num_entrada:
        return jsonify({"msg": "Número de entrada no indicado"}), 400
    try:
        existe = Entrada.query.filter_by(num_entrada=num_entrada).first()
    except Exception as e:
        print(e)

    if existe:
        return jsonify({"msg": f"La entrada {num_entrada} ya existe"}), 400

    entrada = Entrada(num_entrada=num_entrada, dni=dni)
    db.session.add(entrada)
    try:
        db.session.commit()
        data = { "entrada": entrada.to_dict(), "msg":f"La entrada {num_entrada} ha sido añadida"}
        return jsonify(data), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"No se pudo añadir la entrada: {num_entrada}: {e}")
        data = {"msg": f"No se pudo añadir la entrada: {num_entrada}"}
        return jsonify(data), 400


# =========================
# LIST ALL
# =========================
@entradas_bp.route("", methods=["GET"])
@jwt_required()
def list_all():
    rows = Entrada.query.all()
    return jsonify([e.to_dict() for e in rows])


# =========================
# GET BY ID
# =========================
@entradas_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get(id):
    entrada = Entrada.query.get(id)

    if not entrada:
        return jsonify({"msg": f"Entrada {id} no existe"}), 404

    return jsonify({"entrada": entrada.to_dict()})


# =========================
# DELETE BY ID
# =========================
@entradas_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@roles_required("ADMIN")
def delete(id: int):

    entrada = Entrada.query.get(id)
    if not entrada:
        data = {"msg": f"La entrada de id {id} no existe"}
        return jsonify(data), 404

    try:
        entrada_dict = entrada.to_dict()
        db.session.delete(entrada)
        db.session.commit()
        data = {
            "entrada": entrada_dict,
            "msg": f"Entrada con id {id} eliminada"
        }
        return jsonify(data), 200
    except Exception as e:
        db.session.rollback()
        data = {"msg": f"La entrada de id {id} no fué eliminada"}
        return jsonify(data), 400


# =========================
# UPDATE BY ID
# =========================
@entradas_bp.route("/<int:id>", methods=["PUT"])
@require_json
@jwt_required()
@roles_required("ADMIN")
def update(id: int):

    payload  = request.get_json()
    entrada = Entrada.query.get(id)

    if not entrada:
        return jsonify({"msg": f"La entrada de id {id} no existe"}), 404

    num_entrada = payload.get("num_entrada")
    dni = payload.get("dni")

    if not num_entrada:
        data = {"msg": f"Número de entrada no indicado"}
        return jsonify(data), 400

    existe = Entrada.query.filter_by(num_entrada=num_entrada).first()
    if existe and existe.id != id:
        return jsonify({"msg": "Ya existe esa entrada"}), 400

    entrada.num_entrada = num_entrada
    entrada.dni = dni

    try:
        db.session.commit()
        data = {
            "entrada": entrada.to_dict(),
            "msg": f"Entrada con id {id} actualizada"
        }
        return jsonify(data), 200
    except Exception as e:
        db.session.rollback()
        data = {"msg": f"La entrada de id {id} no fué actualizada"}
        return jsonify(data), 400