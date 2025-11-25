class Libro:
    # mensajes_categorias = ( "Tu libro no tiene categoria",
    #                "Tu libro es de una categoria llameante",
    #                "Tu libro es de una categoria inspirada en la Edad Media",
    #             "Tu libro es de una categoria inspirada en la Edad Media")
    # categorias = ("", "Dragones", "Caballeros","Princesas")

    categorias ={
        "-": "Tu libro no tiene categoria",
        "Dragones": "Tu libro es de una categ︃oria llameante",
        "Caballeros":"Tu libro es de una categoria inspirada en la Edad Media",
        "Princesas": "Tu libro es de una categoria inspirada en la Edad Media"
    }

    def __init__(self, titulo,autor,categoria=""):
        self.titulo = titulo
        self.autor = autor
        self.categoria=categoria


    def info(self):
        return f"El libro se llama {self.titulo} y su autor es {self.autor} con la categoria {self.categoria or 'SIN CATEGORIA'}"
    # def validar_categoria(self):
    #     match self.categoria:
    #         case "":
    #             return "Tu libro no tiene categoria"
    #         case "Dragones":
    #             return "Tu libro es de una categoria llameante"
    #         case "Caballeros"|"Princesas":
    #             return "Tu libro es de una categoria inspirada en la Edad Media"

 # def validar_categoria(self):
 #        match self.categoria:
 #            case "":
 #                return Libro.categorias["-"︃]
 #            case "Dragones":
 #                return Libro.categorias["Dragones"︃]
 #            case "Caballeros":
 #                return Libro.categorias[2]
 #            case "Princesas":
 #                return Libro.categorias[3]
 #                return "Tu libro es de una categoria inspirada en la Edad Media"
