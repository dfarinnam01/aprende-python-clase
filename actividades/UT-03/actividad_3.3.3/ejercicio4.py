metros_recorridos=int(input("Cuantas metros has recorrido?"))
vueltas= metros_recorridos //400
metros_restantes=400 -(metros_recorridos %400)
print(f"Has dado {vueltas} vueltas")
print(f"Te han quedado {metros_restantes} metros restantes para otra vuelta")