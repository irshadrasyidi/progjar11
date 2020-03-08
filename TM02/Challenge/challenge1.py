import socket
import sys

server_address = ('10.151.254.22', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

try:
    while True:
        client_socket, client_address = server_socket.accept()

        data = client_socket.recv(1024).decode()

        with open("log.txt", "a+") as openFile:
            openFile.write("Informasi koneksi: " + str(client_socket) + "\n" + "Isi: " + str(data) + "\n\n")

        client_socket.close()

except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)