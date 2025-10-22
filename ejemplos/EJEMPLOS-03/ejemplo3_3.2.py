x="10"
y = int(x) # convierte la cadena "10" a número entero 10
print(y, type(y)) # 10 <class 'int'>

print(x+x)
print(y+y)
# int("3.14") # Error, no se puede convertir directamente a entero
int(3.14) # 3, truncando el decimal
x = "3.14"
y = float(x) # 3.14 como float
z = float(5) # 5 se convierte a 5.0
x = 10
y = str(x) # "10"
z = str(3.14) # "3.14"
bool(0) # False
bool(1) # True
bool("") # False
bool("hola") # True
bool([]) # False
bool([1,2]) # True
lista = [1, 2, 3]
tupla = tuple(lista) # (1, 2, 3)
conjunto = set(lista) # {1, 2, 3}
lista2 = list(tupla) # [1, 2, 3]