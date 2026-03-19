import sys
import logging
from faker import Faker
from libros_dao import LibrosDao
import random

fake=Faker("es_ES")
dao = LibrosDao()
total=10000
for i in range(total):
    libro={
        "isbn": fake.isbn13(),
        "titulo": fake.sentence(nb_words=5),
        "autor": fake.name(),
        "editorial": fake.company(),
        "fecha_publicacion": random.randint(1900,2026),
        "descripcion": fake.text(max_nb_chars=200),
    }
    dao.add(libro)
print("Generacion completada")