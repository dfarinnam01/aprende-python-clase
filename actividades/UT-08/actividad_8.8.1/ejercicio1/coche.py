from vehiculo import Vehiculo
class Coche(Vehiculo) :
    def __init__(self,marca,modelo,color,numero_ruedas,num_puertas):
        super().__init__(marca, modelo, color,numero_ruedas)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Color:",self.color)
        print("Numero de Ruedas:",self.numero_ruedas)
        print("Numero:",self.num_puertas)
        
    def tipo_vehiculo(self):
        print("Soy un coche")