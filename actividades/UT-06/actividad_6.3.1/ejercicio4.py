def update_persona(nif,**kwargs):
    print("Nif: ",nif)
    if kwargs.get("nombre"):
        print("Nombre: ",kwargs["nombre"])
    if kwargs.get("apellido1"):
        print("Apellido1: ",kwargs["apellido1"])
    if kwargs.get("apellido2"):
        print("Apellido2: ",kwargs["apellido2"])
update_persona(123453,nombre="david")

personas = {
    '123':{
        'nif':'123',
        'nombre':'david',
        'apellido1':'123',
        'apellido2':'123'},
    '124':{
        'nif':'123',
        'nombre':'david',
        'apellido1':'123',
        'apellido2':'123'},
}
def update_persona(nif,**datos):
    print(personas.get(nif))
    if personas.get(nif):
        for k,v in datos.items():
            personas[nif][k] = v
update_persona(123,apellido1=123)
