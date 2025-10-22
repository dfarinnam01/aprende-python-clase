cantidad = float(input("Introduce cantidad: "))

num_bill_500=0
num_bill_200=0
num_bill_100=0
num_bill_50=0
num_bill_20=0
num_bill_10=0
num_bill_5=0
num_mon_2=0
num_mon_1=0
num_cent_50=0
num_cent_20=0
num_cent_10=0
num_cent_5=0
num_cent_2=0
num_cent_1=0
if cantidad >=500:
    num_bill_500=cantidad // 500
    cantidad =cantidad - num_bill_500*500
if cantidad >=200:
    num_bill_200=cantidad // 200
    cantidad =cantidad - num_bill_200*200
if cantidad >=100:
    num_bill_100=cantidad // 100
    cantidad =cantidad - num_bill_100*100
if cantidad >=50:
    num_bill_50=cantidad // 50
    cantidad =cantidad - num_bill_50*50
if cantidad >=20:
    num_bill_20=cantidad // 20
    cantidad =cantidad - num_bill_20*20
if cantidad >=10:
    num_bill_10=cantidad // 10
    cantidad =cantidad - num_bill_10*10
if cantidad >=5:
    num_bill_5=cantidad // 5
    cantidad =cantidad - num_bill_5*5
if cantidad >=2:
    num_mon_2=cantidad // 2
    cantidad =cantidad - num_mon_2*2
if cantidad >=1:
    num_mon_1=cantidad // 1
    cantidad =cantidad - num_mon_1*1

cantidad = round(cantidad * 100)

# Monedas en céntimos
if cantidad >= 50:
    num_cent_50 = cantidad // 50
    cantidad =cantidad -  num_cent_50 * 50
if cantidad >= 20:
    num_cent_20 = cantidad // 20
    cantidad =cantidad - num_cent_20 * 20
if cantidad >= 10:
    num_cent_10 = cantidad // 10
    cantidad =cantidad -  num_cent_10 * 10
if cantidad >= 5:
    num_cent_5 = cantidad // 5
    cantidad =cantidad -  num_cent_5 * 5
if cantidad >= 2:
    num_cent_2 = cantidad // 2
    cantidad =cantidad -  num_cent_2 * 2
if cantidad >= 1:
    num_cent_1 = cantidad


print(f"Total de Billetes de 500: {num_bill_500}")
print(f"Total de Billetes de 200: {num_bill_200}")
print(f"Total de Billetes de 100: {num_bill_100}")
print(f"Total de Billetes de 50: {num_bill_50}")
print(f"Total de Billetes de 20: {num_bill_20}")
print(f"Total de Billetes de 10: {num_bill_10}")
print(f"Total de Billetes de 5: {num_bill_5}")
print(f"Total de Monedas de 2: {num_mon_2}")
print(f"Total de Monedas de 1: {num_mon_1}")
print(f"Total de Cents de 50: {num_cent_50}")
print(f"Total de Cents de 20: {num_cent_20}")
print(f"Total de Cents de 10: {num_cent_10}")
print(f"Total de Cents de 5: {num_cent_5}")
print(f"Total de Cents de 2: {num_cent_2}")
print(f"Total de Cents de 1: {num_cent_1}")
