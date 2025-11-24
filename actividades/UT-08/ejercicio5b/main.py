import producto as prod
producto1=prod.producto("Melon",2.50,2,1)
producto2=prod.producto("Sandia",3,4,2)


for i in range(3)
    nombre=input("Ingrese el nombre: ")
    precio=input("Ingrese el precio: ")
    cantidad=input("Ingrese la cantidad del producto: ")
    precio_compra=input("Ingrese el precio de la compra: ")
    producto=prod.producto(nombre,precio,cantidad,precio_compra)
    productos.append(producto)
productos=[producto1,producto2]
ganancia_total=0
for producto in productos:
    producto.aumentar_stock(2)
    ganancia_total+=producto.ganancia_prevista()
print(ganancia_total)