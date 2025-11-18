lista_usuarios = [
    {"usuario": "Juan", "contrasena": "1234", "correo": "juan@gmail.com"},
    {"usuario": "Pablo", "contrasena": "456", "correo": "pablo@gmail.com"}
]
_intentos_usuarios={}
INTENTOS_MAX=3
def index (usuario_introducido):



    # for i, usuario in enumerate(lista_usuarios):
    #     if usuario["usuario"] == usuario_introducido:
    #         return i
    # return -1

    return next((i for i,u in enumerate(lista_usuarios) if u["usuario"] == usuario_introducido), -1)

def exists (usuario_introducido):
    return index(usuario_introducido)

def get(usuario_introducido):
    '''Devolver True si el usuario es valido'''
    return(u for u in lista_usuarios if u["usuario"] == usuario_introducido),None

def login(usuario_introducido,contrasena):
    '''Devuelve True si el usuario es valido'''
    pass
def get_intentos(usuario_introducido):
    '''Devuelve el numero de intentos o 0 si no existe'''
    if _intentos_usuarios[usuario_introducido]:
        return _intentos_usuarios[usuario_introducido]
    return 0
def set_intentos(usuario_introducido,intentos):
    _intentos_usuarios[usuario_introducido] = 0
    pass
def reset_intentos(usuario_introducido,intentos):
    _intentos_usuarios[usuario_introducido] = 0
def inc_intentos(usuario_introducido,intentos):
    '''Inrementa el numero de intentos'''
    _intentos_usuarios[usuario_introducido] +=1
def excedidos_intentos(usuario_introducido):
    '''Devuelve true si se ha excedido el numero de intentos'''
    pass
