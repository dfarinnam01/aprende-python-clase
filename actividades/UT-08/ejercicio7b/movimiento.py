class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.fecha} | {self.tipo} | {self.concepto} | {self.cantidad}€"