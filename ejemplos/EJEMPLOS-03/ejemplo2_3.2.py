nombre, apellidos = 'Francisco Javier', 'Garcia'
pagina, linea = 10, 5
asistentes_lunes, asistentes_miercoles, asistentes_viernes= [50, 40, 80]
c, c2, c3, c4 = 'HOLA'
num_notas = nota_media = mayor_nota = 0
print(c, c2, c3, c4)
print(num_notas)

nombre:str=5
print(nombre)
print(type(nombre))

def saludar(nombre: str, edad: int) -> str:
    return f"Hola, {nombre}. Tienes {edad} años."
print(saludar('David', 18))