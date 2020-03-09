import socket
import select
import sys
import msvcrt
import time
import os

BUFFER_SIZE = 2048
filename = ""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '192.168.0.103'
port = 8081
server.connect((ip_address, port))
while True:
    socket_list = [server]
    read_socket, write_socket, error_socket = select.select(socket_list, socket_list, [])
    if msvcrt.kbhit():
        read_socket.append(sys.stdin)
        # read_socket.insert(0, sys.stdin)

    for socks in read_socket:
        if socks == server:
            message = socks.recv(BUFFER_SIZE).decode('utf-8')
            if str(message):
                filename, filesize = message.split()
                # socks.send("Ok".encode('utf-8'))
                data = socks.recv(int(filesize))
                with open(filename, 'wb') as openFile:
                    openFile.write(data)
        else:
            filename = sys.stdin.readline()
            filename = filename.strip('\n')
            filesize = os.path.getsize(filename)
            server.send(f"{filename} {filesize}".encode())
            print(server.recv(BUFFER_SIZE).decode())

            with open(filename, "rb") as openFile:
                while True:
                    bytes_read = openFile.read(filesize)
                    if not bytes_read:
                        break
                    server.sendall(bytes_read)

            sys.stdout.write('<You send> ')
            sys.stdout.write(filename)
            sys.stdout.write("\n")
            sys.stdout.flush()
            # write(socks)

server.close()
