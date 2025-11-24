import Persona
persona = Persona.Persona("David",21)
persona.saludo()

if persona.mayor_edad():
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")
persona.cambia_dni("80238696")
print(persona.dni)
