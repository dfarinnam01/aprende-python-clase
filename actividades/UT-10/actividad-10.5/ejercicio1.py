import pandas as pd
import numpy as np
from datetime import datetime

# 1️⃣ Crear los números del 0 al 49
datos = np.arange(50)

# 2️⃣ Convertirlos en matriz de 10 filas y 5 columnas
matriz = datos.reshape(10, 5)

# 3️⃣ Crear índice de fechas empezando en hoy
fecha_inicio = datetime.now().date()
fechas = pd.date_range(start=fecha_inicio, periods=10)

# 4️⃣ Crear el DataFrame
df = pd.DataFrame(
    matriz,
    index=fechas,
    columns=["A", "B", "C", "D", "E"]
)

print(df)