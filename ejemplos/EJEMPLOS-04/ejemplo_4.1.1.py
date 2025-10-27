ANSI_AZUL = "\033[34m"
ANSI_VERDE = "\033[32m"
ANSI_ROJO = "\033[31m"
ANSI_RESET = "\033[0m"



num_alumnos= int(input(f"{ANSI_AZUL}Ingrese el numero de alumnos: {ANSI_RESET}"))
notas_alumnos=[]

num_validas=0
num_aprobados=0
for i in range(num_alumnos):
    nota=int(input(f"{ANSI_AZUL}Ingrese la nota del alumno {i+1} :{ANSI_RESET} "))
    if nota < 0:
        print(f"\t{ANSI_ROJO}->Nota incorrecta{ANSI_RESET}")
    else:
        notas_alumnos.append(nota)
        num_validas=num_validas+1
        if nota >=5:
            num_aprobados=num_aprobados + 1

if num_validas>0:
    media_alumnos=sum(notas_alumnos)/num_validas
    porcentaje_aprobados=num_aprobados/num_validas*100

    print(f"{ANSI_VERDE}="*50,f"{ANSI_RESET}")
    print(f"{ANSI_AZUL}Numero de alumnos aprobados:{ANSI_RESET} {num_aprobados}")
    print(f"{ANSI_AZUL}Numero de alumnos suspensos:{ANSI_RESET} {num_validas-num_aprobados}")
    print(f"{ANSI_AZUL}Numero de alumnos validas:{ANSI_RESET} {num_validas}")
    print(f"{ANSI_AZUL}Numero de alumnos desechada:{ANSI_RESET} {num_alumnos-num_validas}")

    print(f"{ANSI_AZUL}La media de alumnos:{ANSI_RESET}",media_alumnos,
          f"{ANSI_VERDE}MEDIA APROBADA{ANSI_RESET}"if media_alumnos >= 5 else
          f"{ANSI_ROJO}MEDIA NO APROBADA{ANSI_RESET}")

    print(f"{ANSI_AZUL}La porcentaje de aprobados es de {ANSI_RESET}{porcentaje_aprobados:.2f}%")
else:
    print("No se ha introducido ninguna nota valida")