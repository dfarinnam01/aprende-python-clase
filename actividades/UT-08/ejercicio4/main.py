import Vehiculo as v
obj_vehiculo = v.Vehiculo("Seat","Panda",20)

obj_vehiculo.acelerar(15)
obj_vehiculo.frenar(5)
obj_vehiculo.cambiar_color("rojo")

print(obj_vehiculo.velocidad)
print(obj_vehiculo.color)