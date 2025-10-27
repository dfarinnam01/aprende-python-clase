ANSI_AZUL = "\033[34m"
ANSI_VERDE = "\033[92m"
ANSI_ROJO = "\033[31m"
ANSI_AMARILLO = "\033[33m"
ANSI_CYAN = "\033[36m"
ANSI_RESET = "\033[0m"

empresa={
    "nombre":input(f"{ANSI_AZUL}Nombre de la empresa:{ANSI_RESET} "),
    "nif":input(f"{ANSI_AZUL}Nif de la empresa:{ANSI_RESET} "),
}
cliente={
    "nombre":input(f"\n{ANSI_AZUL}Nombre del cliente:{ANSI_RESET} "),
    "nif":input(f"{ANSI_AZUL}Nif del cliente:{ANSI_RESET}"),
}

descuento=int(input(f"\n{ANSI_AZUL}Descuento:{ANSI_RESET} "))
print(f"{ANSI_AMARILLO}¡Tambien se aplicará el IVA a los productos!{ANSI_RESET}")
articulos=[]
num_articulos=3
IVA=1.21

print(f"\n{ANSI_ROJO}=== DATOS DE LOS ARTÍCULOS ==={ANSI_RESET}")
for i in range(num_articulos):
    print(f"\n{ANSI_VERDE}Artículo {i+1}{ANSI_RESET}")
    descripcion = input(f"{ANSI_AZUL}Descripción del artículo: {ANSI_RESET}")
    precio = float(input(f"{ANSI_AZUL}Precio sin iva y sin descuento: {ANSI_RESET}")) *IVA
    cantidad = int(input(f"{ANSI_AZUL}¿Cuantos quieres?{ANSI_RESET}"))
    precio_con_desc_cant=(precio-(precio*descuento/100))*cantidad
    precio_redondeado = round(precio_con_desc_cant, 2)
    articulos.append({"descripcion": descripcion, "precio":  precio_redondeado,"cantidad":cantidad})

factura=0
for i in range(num_articulos):
    factura=factura+articulos[i]["precio"]

#print(f"Cliente {cliente['nombre']} con nif:{cliente['nif']} en la empresa {empresa['nombre']} con nif:{empresa['nif']}"
# f" su factura es de {factura:.2f}€")

print(f"{ANSI_VERDE}--------------FACTURA-------------------{ANSI_RESET}")
print(f"{ANSI_CYAN}Empresa {empresa['nombre']} con nif:{empresa['nif']}{ANSI_RESET}")
print(f"{ANSI_CYAN}Cliente {cliente['nombre']} con nif:{cliente['nif']}{ANSI_RESET}\n")
for i in range(num_articulos):
    print(f"{articulos[i]['descripcion']} {articulos[i]['precio']}  {articulos[i]["cantidad"]}")
print(f"{ANSI_VERDE}----------------------------------------{ANSI_RESET}")
print(f"{ANSI_ROJO}       Precio total {factura:.2f}{ANSI_RESET}")
print(f"{ANSI_VERDE}----------------------------------------{ANSI_RESET}")