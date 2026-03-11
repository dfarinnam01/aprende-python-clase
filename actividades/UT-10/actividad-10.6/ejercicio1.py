import pandas as pd

df = pd.read_csv("titanic.csv")

total_pasajeros = len(df)



# 1. Porcentaje de mujeres que sobrevivieron
mujeres = df[df["Sex"] == "female"]
mujeres_supervivientes = mujeres[mujeres["Survived"] == 1]
porcentaje_mujeres = (len(mujeres_supervivientes) / len(mujeres)) * 100
print("Porcentaje de mujeres que sobrevivieron:", porcentaje_mujeres)

# 2. Porcentaje de personas < 15 años que sobrevivieron
menores = df[df["Age"] < 15]
menores_supervivientes = menores[menores["Survived"] == 1]
porcentaje_menores = (len(menores_supervivientes) / len(menores)) * 100
print("Porcentaje menores de 15 que sobrevivieron:", porcentaje_menores)

# 3. Primera clase
clase1 = df[df["Pclass"] == 1]
clase1_supervivientes = clase1[clase1["Survived"] == 1]
print("Primera clase supervivientes:", len(clase1_supervivientes))
print("Porcentaje primera clase:", (len(clase1_supervivientes) / len(clase1)) * 100)

# 4. Segunda clase
clase2 = df[df["Pclass"] == 2]
clase2_supervivientes = clase2[clase2["Survived"] == 1]
print("Segunda clase supervivientes:", len(clase2_supervivientes))
print("Porcentaje segunda clase:", (len(clase2_supervivientes) / len(clase2)) * 100)

# 5. Tercera clase
clase3 = df[df["Pclass"] == 3]
clase3_supervivientes = clase3[clase3["Survived"] == 1]
print("Tercera clase supervivientes:", len(clase3_supervivientes))
print("Porcentaje tercera clase:", (len(clase3_supervivientes) / len(clase3)) * 100)

# 6. SibSp < 3
sib = df[df["SibSp"] < 3]
sib_supervivientes = sib[sib["Survived"] == 1]
print("Porcentaje SibSp < 3:", (len(sib_supervivientes) / len(sib)) * 100)

# 7. Parch < 2
parch = df[df["Parch"] < 2]
parch_supervivientes = parch[parch["Survived"] == 1]
print("Porcentaje Parch < 2:", (len(parch_supervivientes) / len(parch)) * 100)



def calcular_porcentaje(filtro):
    subset = df[filtro]
    supervivientes = subset[subset["Survived"] == 1]
    if len(subset) == 0:
        return 0
    return (len(supervivientes) / len(subset)) * 100


print("\nCONDICIONES COMBINADAS")

print("Mujeres primera clase:",
      calcular_porcentaje((df["Sex"]=="female") & (df["Pclass"]==1)))

print("Mujeres segunda clase:",
      calcular_porcentaje((df["Sex"]=="female") & (df["Pclass"]==2)))

print("Mujeres tercera clase:",
      calcular_porcentaje((df["Sex"]=="female") & (df["Pclass"]==3)))

print("Hombres primera clase:",
      calcular_porcentaje((df["Sex"]=="male") & (df["Pclass"]==1)))

print("Hombres segunda clase:",
      calcular_porcentaje((df["Sex"]=="male") & (df["Pclass"]==2)))

print("Hombres tercera clase:",
      calcular_porcentaje((df["Sex"]=="male") & (df["Pclass"]==3)))

print("Mujeres con SibSp <4 y Parch <4:",
      calcular_porcentaje((df["Sex"]=="female") & (df["SibSp"]<4) & (df["Parch"]<4)))

print("Pasajeros segunda clase con SibSp <2 y Parch <2:",
      calcular_porcentaje((df["Pclass"]==2) & (df["SibSp"]<2) & (df["Parch"]<2)))

print("Hombres con SibSp <3 y Parch ==3:",
      calcular_porcentaje((df["Sex"]=="male") & (df["SibSp"]<3) & (df["Parch"]==3)))