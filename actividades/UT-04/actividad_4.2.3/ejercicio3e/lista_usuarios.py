lista_usuarios = [
    {"usuario": "Juan", "contrasena": "1234", "correo": "juan@gmail.com"},
    {"usuario": "Pablo", "contrasena": "456", "correo": "pablo@gmail.com"}
]

_intentos_usuarios = {}
INTENTOS_MAX = 3


def index(usuario_introducido):
    """Devuelve el índice del usuario o -1 si no existe."""
    return next((i for i, u in enumerate(lista_usuarios) if u["usuario"] == usuario_introducido), -1)


def exists(usuario_introducido):
    """Devuelve True si el usuario existe."""
    return index(usuario_introducido) != -1


def get(usuario_introducido):
    """Devuelve el diccionario del usuario o None si no existe."""
    return next((u for u in lista_usuarios if u["usuario"] == usuario_introducido), None)


def login(usuario_introducido, contrasena):
    """Devuelve True si usuario y contraseña son correctos."""
    usuario = get(usuario_introducido)
    return usuario is not None and usuario["contrasena"] == contrasena


def get_intentos(usuario_introducido):
    """Devuelve el número de intentos o 0 si no existe registro."""
    return _intentos_usuarios.get(usuario_introducido, 0)


def set_intentos(usuario_introducido, intentos):
    """Establece el número de intentos."""
    _intentos_usuarios[usuario_introducido] = intentos


def reset_intentos(usuario_introducido):
    """Reinicia intentos a 0."""
    _intentos_usuarios[usuario_introducido] = 0


def inc_intentos(usuario_introducido):
    """Incrementa el número de intentos."""
    _intentos_usuarios[usuario_introducido] = get_intentos(usuario_introducido) + 1


def excedidos_intentos(usuario_introducido):
    """Devuelve True si el usuario ha excedido el número de intentos."""
    return get_intentos(usuario_introducido) >= INTENTOS_MAX
