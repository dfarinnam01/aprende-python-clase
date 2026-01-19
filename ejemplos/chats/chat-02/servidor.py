import socket

entradas=[]

# HOST = '127.0.0.1'#si solo queremos aceptar conexiones localhost
HOST = '192.168.60.204'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))#nos conectamos pa
server.listen() #espera una conexion
print("Servidor esperando conexion...")
conn, addr = server.accept()
print("Conexion con: ",addr)

while True:
    pdu = conn.recv(1024).decode()
    campos=pdu.split(":")
    print("Cliente: ", pdu)

    if campos[0] == 0:
        print("Cliente se desconecto...")
        break
    elif campos[0] == 1:
        entrada=campos[1]
        if entrada in entradas:
            pdu=f"-2:{entrada}"
        else:
            entradas.append(entrada)
            pdu=f"-3:{entrada}"
    conn.send(pdu.encode())