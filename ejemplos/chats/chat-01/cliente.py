import socket

HOST_DESTINO = '192.168.60.207'
PORT_DESTINO = 65432
'''socket.AF_INET indica IPv4
socket.AF_INET6 indica IPV6
socket.SOCK_STREAM indica TCP
socket.SOCK_DGRAM indica UDP'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_DESTINO, PORT_DESTINO))
while True:
    mensaje=input("Cliente: ")
    client.send(mensaje.encode())
    if mensaje.lower() == "salir":
        print("Saliendo...")
        break
    respuesta = client.recv(1024).decode()
    print("Servidor: ", respuesta)
