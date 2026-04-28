from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Viaje(db.Model):
    __tablename__ = 'viajes'
    id = db.Column(db.Integer, primary_key=True)
    # TITULO NO DEBERÍA SER UNIQUE. SOLO A NIVEL APRENDIZAJE
    titulo = db.Column(db.String(100), unique=True, nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text(100), nullable=False)
    fecha_viaje = db.Column(db.DateTime, nullable=False)
    duracion_dias = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Numeric(10,2), nullable=False)
    foto_nombre = db.Column(db.String(200))
    foto_miniatura = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Viaje {self.titulo}>'

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'destino': self.destino,
            'descripcion': self.descripcion,
            'fecha_viaje': self.fecha_viaje.strftime('%d/%m/%Y %H:%M'),
            'duracion_dias': self.duracion_dias,
            'precio': self.precio,
            'foto_nombre': self.foto_nombre,
            'foto_miniatura': self.foto_miniatura,
        }