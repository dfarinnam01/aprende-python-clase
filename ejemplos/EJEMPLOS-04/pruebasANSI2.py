import random
import time

BORRA_LINEA= '\033[2k'
CURSOR_INICIO= '\033[1G'

for i in range (1,100):
    numero= random.randint(1,100)
    #print(numero)
    print(f"{BORRA_LINEA}{CURSOR_INICIO}Numero aleatorio: {numero}",end=' ',flush=True,)
    time.sleep(1)
print("\nFIN DEL PROGRAMA")