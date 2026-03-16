import random
class ArticuloFaker:

    _descripciones = [
        "Martillo",
        "Destornillador plano",
        "Destornillador estrella",
        "Llave inglesa",
        "Llave fija",
        "Llave Allen",
        "Alicates",
        "Alicates de corte",
        "Tenazas",
        "Sierra de mano",
        "Serrucho",
        "Taladro",
        "Broca para metal",
        "Broca para madera",
        "Broca para pared",
        "Tornillos",
        "Tornillos para madera",
        "Tornillos para metal",
        "Clavos",
        "Tacos de pared",
        "Cinta métrica",
        "Nivel de burbuja",
        "Escuadra",
        "Lima metálica",
        "Lija",
        "Lija para madera",
        "Lija para metal",
        "Cutter",
        "Cuchilla de repuesto",
        "Pistola de silicona",
        "Barra de silicona",
        "Pegamento fuerte",
        "Pegamento para madera",
        "Cinta aislante",
        "Cinta americana",
        "Candado",
        "Bisagras",
        "Cerrojo",
        "Manilla de puerta",
        "Rueda para mueble",
        "Rodillo de pintura",
        "Brocha",
        "Espátula",
        "Cubeta de pintura",
        "Masilla",
        "Sellador",
        "Tornillo de banco",
        "Abrazadera",
        "Escalera plegable",
        "Guantes de trabajo"
    ]
    _observaciones =''' Lorem ipsum dolor sit amet, consectetur adipiscing elit.
     Cras luctus mattis vestibulum. Nunc nec eros et nisl mattis vehicula.
      Donec finibus lorem odio, at laoreet sem tristique in.
      '''
    @staticmethod
    def _generar_referencia():
        return random.randint(10000000,99999999)

    @staticmethod
    def _generar_precio():
        return round(random.uniform(1.5, 250),2)

    @staticmethod
    def _generar_stock():
        return round(random.uniform(0, 500),3)

    @classmethod
    def _generar_descripcion(cls):
        return random.choice(cls._descripciones)

    @classmethod
    def _generar_observaciones(cls,num_palabras=15):
        palabras = cls._observaciones.split()
        return " ".join(random.sample(palabras,num_palabras))

    @classmethod
    def generar(cls):
        return {
            "referencia": cls._generar_referencia(),#"referencia": ArticuloFaker._generar_referencia(),
            "descripcion":cls._generar_descripcion(),
            "precio":cls._generar_precio(),
            "stock":cls._generar_stock(),
            "observacion":cls._generar_observaciones(),
        }
    @classmethod
    def generar_lote(cls,n):
        return [cls.generar() for _ in range(n)]

if __name__ == '__main__':
    print(ArticuloFaker.generar())