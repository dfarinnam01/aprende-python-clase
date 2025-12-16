import socket

HOST = '127.0.0.1'
PORT = 65432
'''socket.AF_INET indica IPv4
socket.AF_INET6 indica IPV6
socket.SOCK_STREAM indica TCP
socket.SOCK_DGRAM indica UDP'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))#nos conectamos pa
server.listen() #espera una conexion
print("Servidor esperando conexion...")
conn, addr = server.accept()
print("Conexion con: ",addr)

while True:
    mensaje = conn.recv(1024).decode()
    print("Cliente: ",mensaje)

    respuesta = input("Servidor: ")
    conn.send(respuesta.encode())