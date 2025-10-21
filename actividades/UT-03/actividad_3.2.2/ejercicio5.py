ticket = {'plato_pedido': "Solomillo iberico", 'precio_unitario': 16.3, 'cantidad': 6}
ticket['total_pagar']=ticket['precio_unitario']*ticket['cantidad']

print("                       BURGER KING")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("                       TOTAL COMPRA")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"                {ticket['cantidad']} {ticket['plato_pedido']} {ticket['precio_unitario']}")
print(f"Total a pagar: {ticket['total_pagar']}")