import funciones_asistentes as f
salida=0
while salida!=1:
    opcion=f.menu()
    match opcion:
        case 1:
            f.nuevo_libro()
        case 2:
            f.consulta()
        case 3:
            f.listado()
        case 4:
            f.borrar
        case 0:
            salida=1
            print("FIN DEL PROGRAMA")