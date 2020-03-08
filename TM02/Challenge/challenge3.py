import socket
import sys
import os

BUFFER_SIZE = 128

server_address = ('10.151.254.22', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

try:
    while True:
        client_socket, client_address = server_socket.accept()

        data = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = data.split()
        client_socket.sendall("response: ok".encode())
        with open(filename, "a+") as openFile:
            # for i in range(float(filesize) / float(BUFFER_SIZE)):
            i = 0
            while i <= int(filesize):
                data = client_socket.recv(BUFFER_SIZE).decode()
                openFile.write(data)
                i += BUFFER_SIZE

        print("Packet received")

        client_socket.close()

except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)