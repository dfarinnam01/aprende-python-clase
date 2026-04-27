from functools import wraps
from flask import jsonify, request
from flask_jwt_extended import get_jwt

def roles_required(*roles):
    '''
    Ejemplos de uso:
        @roles_required("ADMIN")
        @roles_required("USER", "EMPLEADO")
        debe indicarse en el siguiente orden:
            @jwt_required()
            @role_required("ADMIN")
    '''
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()

            if claims.get("role") not in roles:
                return jsonify({"msg": f"Acceso autorizado solo a roles: {roles}"}), 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper


def require_json(fn):
    '''
    Ejemplos de uso:
        @require_json
    '''
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return jsonify({"msg": "Se requiere JSON"}), 400
        return fn(*args, **kwargs)
    return wrapper