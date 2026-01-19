import socket
import codigos_ansi as CA

HOST_DESTINO = '192.168.60.54'
PORT_DESTINO = 65432
'''socket.AF_INET indica IPv4
socket.AF_INET6 indica IPV6
socket.SOCK_STREAM indica TCP
socket.SOCK_DGRAM indica UDP'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_DESTINO, PORT_DESTINO))
while True:
    mensaje = input(f" ")
    print(f"\t{CA.CodigosAnsi.BG_BRIGHT_GREEN}{mensaje:>80}{CA.CodigosAnsi.RESET}", )
    # print(f"\t{CA.CodigosAnsi.BG_BRIGHT_GREEN}{mensaje}{CA.CodigosAnsi.RESET}",)
    client.send(mensaje.encode())
    if mensaje.lower() == "salir":
        print("Saliendo...")
        break
    respuesta = client.recv(1024).decode()
    print(f"{CA.CodigosAnsi.BG_WHITE}{respuesta}{CA.CodigosAnsi.RESET}")
