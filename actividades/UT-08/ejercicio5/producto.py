class producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = ""
    def aumentar_stock(self,cantidad):
        self.cantidad += cantidad
    def disminuir_stock(self,cantidad):
        self.cantidad=max(self.cantidad - cantidad,0)
    def set_descripcion(self,descripcion):
        self.descripcion = descripcion
