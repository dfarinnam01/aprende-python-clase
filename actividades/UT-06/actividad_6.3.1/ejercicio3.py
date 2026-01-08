def info_persona(nombre,*args,**kwargs):
    print("Nombre: ",nombre)
    print("Otros datos: ",args)
    print("Informacion extra: ",kwargs)
info_persona("David", 25, "Ingeniero", ciudad='Madrid', pais='España')
