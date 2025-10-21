a=2
b=3
#Primera Solución con variable auxiliar
aux=a
a=b
b=aux

print(a)
print(b,"\n")

#Segunda Solución sin variable auxiliar
a , b = b , a

print(a)
print(b)