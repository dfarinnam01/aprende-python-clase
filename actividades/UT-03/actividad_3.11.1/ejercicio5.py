roles = []
for i in range(3):
    rol = input(f"Introduce el rol {i+1} (o presione enter para omitir): ").strip()
    if rol:
        roles.append(rol)
print(roles)
