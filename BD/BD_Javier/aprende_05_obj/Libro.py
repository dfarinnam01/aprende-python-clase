class Libro:
    def __init__(self):
        self.id = id
        self.isbn=None
        self.titulo=None
        self.autor=None
        self.editorial=None
        self.fecha_publicacion=None
        self.descripcion=None

    @staticmethod
    def from_dict(row:dict)->"Libro":
        libro = Libro()
        libro.id = row.get('id',None)
        libro.isbn=row.get('isbn',None)
        return libro