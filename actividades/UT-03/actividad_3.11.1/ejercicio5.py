roles = []
for i in range(3):
    rol = input(f"Ingrese el rol #{i+1} (o presione Enter para omitir): ").strip()
    if rol:
        roles.append(rol)
print("Roles ingresados:", ", ".join(roles))
