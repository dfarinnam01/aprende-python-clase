from db import db

class Entrada(db.Model):
    __tablename__ = "entradas"

    id = db.Column(db.Integer, primary_key=True,index=True)
    num_entrada = db.Column(db.String(10), unique=True, nullable=False)
    dni = db.Column(db.String(10), unique=False, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "num_entrada": self.num_entrada,
            "dni": self.dni
        }
    def __repr__(self):
        return f"Entrada:(id={self.id}, num_entrada={self.num_entrada}, dni={self.dni})"