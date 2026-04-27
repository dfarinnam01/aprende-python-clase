# models.py
from datetime import datetime, timezone

from db import db
from werkzeug.security import generate_password_hash, check_password_hash

# ======================================
# ENTRADAS
# ======================================
class Entrada(db.Model):
    __tablename__ = "entradas"

    id = db.Column(db.Integer, primary_key=True, index=True)
    num_entrada = db.Column(db.String(10), unique=True, nullable=False)
    dni = db.Column(db.String(10), nullable=True)
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    def to_dict(self):
        return {
            "id": self.id,
            "num_entrada": self.num_entrada,
            "dni": self.dni
        }

    def __repr__(self):
        return f"<Entrada(id={self.id}, num_entrada='{self.num_entrada}, dni={self.dni})>')>"



class Usuario(db.Model):
    __tablename__ = "usuarios"

    ROLES = ("USER", "ADMIN")

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), default="USER")  # ADMIN o USER
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def set_role(self, role):
        if role.upper() not in self.ROLES:
            raise ValueError("Rol no válido")
        self.role = role.upper()

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
        }
