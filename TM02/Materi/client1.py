import socket

server_address = ('localhost', 5001)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

strsend = "Hi...."
client_socket.send(strsend.encode())
client_socket.close()