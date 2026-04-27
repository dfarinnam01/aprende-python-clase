# routes/auth.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, get_jwt, jwt_required
from datetime import datetime
import logging

from db import db
from models import Usuario
from decorators import roles_required, require_json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



auth_bp = Blueprint("auth", __name__)

# ############  REGISTER  ############
@auth_bp.route("/register", methods=["POST"])
@require_json
def register():
    payload = request.get_json()

    username = payload.get("username")
    password = payload.get("password")
    role =  "USER"

    if not username or not password:
        return jsonify({"message": "Faltan datos"}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"message": "Usuario ya existe"}), 400

    user = Usuario(username=username, role=role)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"user":user.to_dict(), "message": "Usuario creado"}), 201


# ############  LOGIN  ############
@auth_bp.route("/login", methods=["POST"])
@require_json
def login():
    payload = request.get_json()

    username = payload.get("username")
    password = payload.get("password")

    user = Usuario.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"message": "Credenciales incorrectas"}), 401

    token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role}
    )

    return jsonify({"access_token": token})

# ############  CAMBIA ROL  ############
@auth_bp.route("/role", methods=["PATCH"])
@require_json
@jwt_required()
@roles_required("ADMIN")
def set_role():
    payload = request.get_json()

    username = payload.get("username")
    role = payload.get("role")

    if not username or not role:
        return jsonify({"message": "Faltan datos"}), 400

    if role not in Usuario.ROLES:
        return jsonify({"message": "Rol inválido"}), 400

    user = Usuario.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    try:
        user.role = role
        db.session.commit()
        data = {"user": user.to_dict(), "message": f"El rol del usuario {username} se estableció a {role}"}
        return jsonify(data), 200
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error cambiando rol de {username}: {e}")
        data = {"message": f"No se pudo cambiar el rol al usuario: {username}"}
        return jsonify(data), 400

# ========================================
# ===  ENDPOINTS SOLO  PARA DESARROLLO
# ========================================

# ############  REGISTER  ############
@auth_bp.route("/register-developer", methods=["POST"])
@require_json
def register_developer():
    payload = request.get_json()

    username = payload.get("username")
    password = payload.get("password")
    role = payload.get("role","").upper()

    if not username or not password or not role:
        return jsonify({"message": "Faltan datos"}), 400

    if role not in Usuario.ROLES:
        return jsonify({"message": "Rol inválido"}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"message": "Usuario ya existe"}), 400

    user = Usuario(username=username, role=role)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"user":user.to_dict(), "message": "Usuario creado"}), 201

# ############  LISTAR USUARIOS  ############
@auth_bp.route("/users", methods=["GET"])
@jwt_required()
@roles_required("ADMIN")
def get_users():
    try:
        users = Usuario.query.all()

        data = {
            "users": [user.to_dict() for user in users],
            "count": len(users)
        }
        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error obteniendo usuarios: {e}")
        return jsonify({"message": "Error al obtener usuarios"}), 500

# ############  CONSULTA COMPLETA ROL (SOLO DESARROLLO) ############
@auth_bp.route("/token/full-info", methods=["GET"])
@jwt_required()
def token_full_info():
    identity = get_jwt_identity()
    claims = get_jwt()

    return jsonify({
        "user_id": identity,
        "claims": claims
    })

# ############  CONSULTA SIMPLE ROL  (SOLO DESARROLLO)  ############
@auth_bp.route("/token/simple-info", methods=["GET"])
@jwt_required()
def token_simple_info():
    claims = get_jwt()

    def to_es_date(ts):
        if not ts:
            return None
        return datetime.fromtimestamp(ts).strftime("%d/%m/%Y %H:%M:%S")

    return jsonify({
        "user_id": get_jwt_identity(),
        "role (roles)": claims.get("role"),
        "type": claims.get("type"),
        "jti (identificador)": claims.get("jti"),

        "iat (emitido)": to_es_date(claims.get("iat")),
        "exp (expira": to_es_date(claims.get("exp")),
        "nbf (no valido antes de)": to_es_date(claims.get("nbf")),
    })

