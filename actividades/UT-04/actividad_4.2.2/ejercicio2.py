serie_num=[1,2,3,4,5,6,7,8,9,10]
mayor=0
menor=11
for i in serie_num:
    if i>mayor:
        mayor=i
    if i<menor:
        menor=i
print(mayor,menor)