import producto as prod
producto = prod.producto("Melon",2.23,8)
producto.aumentar_stock(3)
producto.disminuir_stock(2)
producto.set_descripcion("Fruta dulce de buen tamaño parecida a las sandias")
print(producto.cantidad)
print(producto.descripcion)