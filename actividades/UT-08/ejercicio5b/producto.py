class producto:
    def __init__(self,nombre,precio,cantidad=1,precio_compra=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.precio_compra = precio_compra

    def aumentar_stock(self,cantidad):
        self.cantidad += cantidad

    def disminuir_stock(self,cantidad=1):
        stock_final=self.cantidad - cantidad
        if stock_final < 0:
            self.cantidad=0
            return cantidad- self.cantidad
        else:
            self.cantidad=stock_final
            return cantidad
    def ganancia_prevista(self):
        return self.cantidad *self.precio -self.cantidad*self.precio_compra