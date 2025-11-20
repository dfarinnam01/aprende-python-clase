from operator import truediv

lista_usuarios = [
    {"usuario": "Juan", "contrasena": "1234", "correo": "juan@gmail.com"},
    {"usuario": "Pablo", "contrasena": "456", "correo": "pablo@gmail.com"}
]

_intentos_usuarios = {}
INTENTOS_MAX = 3


def index(usuario_introducido):
    return next((i for i, u in enumerate(lista_usuarios) if u["usuario"] == usuario_introducido), -1)


def exists(usuario_introducido):
    return index(usuario_introducido) != -1


def get(usuario_introducido):
    return next((u for u in lista_usuarios if u["usuario"] == usuario_introducido), None)
    #return lista_usuarios[index(usuario_introducido)] if exists(usuario_introducido) else None


def login(usuario_introducido, contrasena):
    usuario = get(usuario_introducido)
    if usuario is not None and usuario["contrasena"] == contrasena:
        return True
    return False


def get_intentos(usuario_introducido):
    return _intentos_usuarios.get(usuario_introducido, 0)


def set_intentos(usuario_introducido, intentos):
    _intentos_usuarios[usuario_introducido] = intentos


def reset_intentos(usuario_introducido):
    _intentos_usuarios[usuario_introducido] = 0


def inc_intentos(usuario_introducido):
    _intentos_usuarios[usuario_introducido] = get_intentos(usuario_introducido) + 1


def excedidos_intentos(usuario_introducido):
    return get_intentos(usuario_introducido) >= INTENTOS_MAX -1
