import random
import logging
from faker import Faker

from db.libros_dao import LibrosDao
from db.editoriales_dao import EditorialesDao
from db.autores_dao import AutoresDao
from utils.cepy_progress_printer import CepyProgressPrinter

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)-8s] [%(name)s] %(message)s',
    filename='errores.log',
    filemode='a',
    encoding='utf-8'
)

fake = Faker("es_ES")

# DAOs
libros_dao = LibrosDao()
editoriales_dao = EditorialesDao()
autores_dao = AutoresDao()

# ======================================
# 1. CREAR EDITORIALES
# ======================================
editoriales_ids = []
for _ in range(20):
    nombre = fake.company()
    eid = editoriales_dao.add({"nombre": nombre})
    if eid != -1:
        editoriales_ids.append(eid)

# ======================================
# 2. CREAR AUTORES
# ======================================
autores_ids = []
for _ in range(50):
    nombre = fake.name()
    aid = autores_dao.add({"nombre": nombre})
    if aid != -1:
        autores_ids.append(aid)

# ======================================
# 3. CREAR LIBROS + RELACIONES
# ======================================
total_fakers = 100
progress = CepyProgressPrinter(msg="Generando libros:", total=total_fakers)

for i in range(1, total_fakers + 1):

    editorial_id = random.choice(editoriales_ids) if editoriales_ids else None

    libro = {
        "isbn": fake.isbn13(),
        "titulo": fake.sentence(nb_words=5),
        "fecha_publicacion": random.randint(1900, 2026),
        "descripcion": fake.text(max_nb_chars=200),
        "editorial_id": editorial_id,
        "autores": random.sample(
            autores_ids,
            k=random.randint(1, 3)  # entre 1 y 3 autores por libro
        )
    }

    # Insertar libro con autores
    libro_id = libros_dao.add(libro)

    # Relacionar autores
    for autor_id in libro["autores"]:
        autores_dao.add_to_libro(libro_id, autor_id)

    progress.update(i)

progress.check_finish()