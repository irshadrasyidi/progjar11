import socket

server_address = ('LAPTOP-8HDTIU3S', 50000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

client_socket.send("Hi".encode())

# print(client_socket.recv(1024).decode())

client_socket.close()