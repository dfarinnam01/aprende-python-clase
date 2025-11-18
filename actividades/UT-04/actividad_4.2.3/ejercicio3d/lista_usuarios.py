lista_usuarios = [
    {"usuario": "Juan", "contrasena": "1234", "correo": "juan@gmail.com"},
    {"usuario": "Pablo", "contrasena": "456", "correo": "pablo@gmail.com"}
]

_intentos_usuarios = {}
INTENTOS_MAX = 3

def index(usuario_introducido):
    """Devuelve el índice del usuario o -1 si no existe"""
    return next((i for i, u in enumerate(lista_usuarios) if u["usuario"] == usuario_introducido), -1)

def exists(usuario_introducido):
    """Devuelve True si el usuario existe"""
    return index(usuario_introducido) != -1

def get(usuario_introducido):
    """Devuelve el diccionario del usuario si existe, None si no"""
    i = index(usuario_introducido)
    return lista_usuarios[i] if i != -1 else None

def login(usuario_introducido, contrasena):
    """
    Devuelve True si el usuario existe y la contraseña es correcta.
    También reinicia intentos si el login es correcto.
    """
    usuario = get(usuario_introducido)
    if usuario and usuario["contrasena"] == contrasena:
        reset_intentos(usuario_introducido)
        return True
    else:
        inc_intentos(usuario_introducido)
        return False

def get_intentos(usuario_introducido):
    """Devuelve el número de intentos o 0 si no existe"""
    return _intentos_usuarios.get(usuario_introducido, 0)

def set_intentos(usuario_introducido, intentos):
    """Establece el número de intentos"""
    _intentos_usuarios[usuario_introducido] = intentos

def reset_intentos(usuario_introducido):
    """Reinicia el número de intentos a 0"""
    _intentos_usuarios[usuario_introducido] = 0

def inc_intentos(usuario_introducido):
    """Incrementa el número de intentos en 1"""
    _intentos_usuarios[usuario_introducido] = get_intentos(usuario_introducido) + 1

def excedidos_intentos(usuario_introducido):
    """Devuelve True si se ha excedido el número máximo de intentos"""
    return get_intentos(usuario_introducido) >= INTENTOS_MAX
