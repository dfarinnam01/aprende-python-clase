nombre_archivo = __file__
with open(nombre_archivo,"r",encoding="utf-8") as f:
    contenido = f.read()
print(contenido)
import locale
print(locale.getpreferredencoding())