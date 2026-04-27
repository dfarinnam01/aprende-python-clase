# app_flask.py
'''
pip install flask-jwt-extended werkzeug
'''

from datetime import timedelta
import logging

from flask import Flask, jsonify
from db import db, init_db
from flask_jwt_extended import JWTManager
from routes_auth import auth_bp
from routes_entradas import entradas_bp


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)

init_db(app)

# crear tablas
with app.app_context():
    db.create_all()

# Mejor:
'''
with app.app_context():
    try:
        db.create_all()
        print("Tablas creadas exitosamente")
    except Exception as e:
        print(f"Error creando tablas: {e}")
'''


app.config["JWT_SECRET_KEY"] = "clave-secreta-cepy-2026"  # IMPORTANTE: cmbiarlo en producción
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
jwt = JWTManager(app)

#############################
#  BLUEPRINTS
#############################
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(entradas_bp, url_prefix="/api/entradas")

#############################
# RUTAS
#############################

@app.route("/")
def home():
    return jsonify({"message": "API de entradas"})

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")