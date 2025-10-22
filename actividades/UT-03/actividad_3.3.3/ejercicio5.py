empresa={
    "nombre":input("Nombre de la empresa: "),
    "nif":input("Nif de la empresa: "),
}
cliente={
    "nombre":input("Nombre del cliente: "),
    "nif":input("Nif del cliente: "),
}

descuento=int(input("Descuento: "))
articulos=[]
num_articulos=3
IVA=1.21

for i in range(num_articulos):
    descripcion = input("Descripción del artículo: ")
    cantidad=int(input("Cuantos quieres?"))
    precio = float(input("Precio sin iva y sin descuento: ")) *IVA
    precio_con_desc=precio-(precio*descuento/100)
    precio_redondeado = round(precio_con_desc, 2)
    articulos.append({"descripcion": descripcion, "precio":  precio_redondeado})

factura=0
for i in range(num_articulos):
    factura=factura+articulos[i]["precio"]

print(f"Cliente {cliente['nombre']} con nif:{cliente['nif']} en la empresa {empresa['nombre']} con nif:{empresa['nif']}"
      f" su factura es de {factura:.2f}€")

print(f"--------------FACTURA-------------------")
print(f"Empresa {empresa['nombre']} con nif:{empresa['nif']}")
print(f"Cliente {cliente['nombre']} con nif:{cliente['nif']}\n")
for i in range(num_articulos):
    print(f"{articulos[i]['descripcion']} {articulos[i]['precio']}")
print(f"       Precio total {factura:.2f}€")
print(f"----------------------------------------")