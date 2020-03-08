import socket

server_address = input("Masukkan IP server: ")
server_port = int(input("Masukkan port server: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))

strsend = "Hi...."
client_socket.send(strsend.encode())
dict = client_socket.recv(1024).decode()
print(str(dict))
client_socket.close()