import numpy as np
numeros = np.array([1,2,3,4,5])
print(numeros)

COLOR_AZUL = '\033[94m'

FIN_COLOR = '\033[0m'

mensaje = "¡Hola! Esta salida está en azul. 💙"

print(COLOR_AZUL + mensaje + FIN_COLOR)

print("Este texto ya no es azul.")