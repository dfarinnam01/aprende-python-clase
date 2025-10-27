ANSI_AZUL = "\033[34m"
ANSI_VERDE = "\033[32m"
ANSI_ROJO = "\033[31m"
ANSI_RESET = "\033[0m"
ANSI_ARRIBA = "\033[F"
ANSI_COLUMNA_40 = "\033[40C"


notas_alumnos=[]
num_aprobados=0
i=0
while nota>=0:
    nota=int(input(f"{ANSI_AZUL}Ingrese la nota del alumno {i+1} :{ANSI_RESET} "))
    if nota >= 0 and nota <= 10:
        notas_alumnos.append(nota)
        if nota >=5:
            num_aprobados=num_aprobados + 1
    i =i+1

    media_alumnos=sum(notas_alumnos)/i
    porcentaje_aprobados=num_aprobados/i*100

    print(f"{ANSI_VERDE}="*50,f"{ANSI_RESET}")
    print(f"{ANSI_AZUL}Numero de alumnos aprobados:{ANSI_RESET} {num_aprobados}")
    print(f"{ANSI_AZUL}Numero de alumnos suspensos:{ANSI_RESET} {i-num_aprobados}")

    print(f"{ANSI_AZUL}La media de alumnos:{ANSI_RESET}",media_alumnos,
          f"{ANSI_VERDE}MEDIA APROBADA{ANSI_RESET}"if media_alumnos >= 5 else
          f"{ANSI_ROJO}MEDIA NO APROBADA{ANSI_RESET}")

    print(f"{ANSI_AZUL}La porcentaje de aprobados es de {ANSI_RESET}{porcentaje_aprobados:.2f}%")
else:
    print("No se ha introducido ninguna nota valida")