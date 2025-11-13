import funciones_asistentes as f
salida=0
datos_entradas = []
while salida!=1:
    opcion=f.menu()
    match opcion:
        case 1:
            f.nueva_entrada()
        case 2:
            f.consulta_entrada()
        case 3:
            f.listado()
        case 0:
            salida=1
            print("FIN DEL PROGRAMA")