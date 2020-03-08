import socket
import select
import sys
from datetime import datetime
import os

# BUFFER_SIZE = 128
server_address = ('10.151.254.118', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

input_socket = [server_socket]

FOLDER = ""

try:
    while True:
        read_ready, write_ready, exception = select.select(input_socket, [], [])

        for sock in read_ready:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                input_socket.append(client_socket)
                FOLDER = client_socket.recv(1024).decode()
                os.mkdir("hasil/" + FOLDER)
            else:
                data = sock.recv(1024).decode()
                # print(filename, filesize)
                if str(data):
                    filename, filesize = data.split()
                    print(filename, filesize)
                    sock.send("Ok".encode())
                    data = sock.recv(int(filesize))
                    with open("hasil/" + FOLDER + "/" + filename, 'wb') as openFile:
                        openFile.write(data)
                    # sock.send("File {} received.".format(filename).encode())
                else:
                    sock.close()
                    input_socket.remove(sock)

except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)