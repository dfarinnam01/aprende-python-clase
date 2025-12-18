import socket

# HOST_DESTINO = '127.0.0.1'
HOST_DESTINO = '192.168.60.54'
PORT_DESTINO = 65432
'''
    Codificaion PDU -> codigo:datos
        Codigo 1: envio de entrada -> 1:nº de entrada (str)
        Codigo 0: cerrar conexion  -> 0:mensaje despedida
        Codigo 2: login            -> 2:usuario:password
        Codigo-1: NACK
        Codigo-2: Entrada existente
        Codigo-3: ACK
'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_DESTINO, PORT_DESTINO))
while True:
    entrada=input("Numero de entrada(0 par salir): ")
    pdu=f"1:{entrada}"
    client.send(pdu.encode())


    if campos[0]== '0':
        print("Saliendo...")
        break
    pdu = client.recv(1024).decode()
    campos = pdu.split(":")
    if campos[0] == "-2":
        print("Entrada no añadida")
    elif campos[0] == "3":
        print("Entrada añadida")
