import logging

from database import Database
from libros_dao import LibrosDao

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)-8s] [%(name)s] %(message)s',
                    filemode='a', filename='errores.log',encoding='utf-8')
logger = logging.getLogger("App")
logger.debug('app started')
dao = LibrosDao()

id=dao.add(
    {"isbn":"978-00-00-000002",
     "titulo":"El Quijote",
     "autor":"Cervantes",
     "editorial":"Desconocida",
     "fecha_publicacion":1600}
)

if id>0:
    print("el id es : ",id)
    libro=dao.get(id)
    print(libro)
else:
    print("No se pudo añadir el libro")
print(dao.get_all())





if __name__ == "__main__":



    db=LibroDB()
    db.add_libro({"isbn":231214,"titulo":"Libro 1","editorial":"Paco y yo","autor":"Paco","fecha_publicacion":15})
    for libro in db.get_all_libros():
        print(libro)
    print(db.get_by_isbn(231214))