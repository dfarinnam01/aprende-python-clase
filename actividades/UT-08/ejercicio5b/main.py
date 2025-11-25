import producto as prod

productos=[]
for i in range(3):
    nombre=input("Ingrese el nombre: ")
    precio=float(input("Ingrese el precio: "))
    cantidad=int(input("Ingrese la cantidad del producto: "))
    precio_compra=float(input("Ingrese el precio de la compra: "))
    producto=prod.producto(nombre,precio,cantidad,precio_compra)
    productos.append(producto)
ganancia_total=0
for producto in productos:
    producto.aumentar_stock(2)
    ganancia_total+=producto.ganancia_prevista()
print("Ganancia total prevista:", ganancia_total)