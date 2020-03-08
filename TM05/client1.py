import socket
import select
import sys
import msvcrt
import time

message = []


# def write(socket):
#     if msvcrt.kbhit():
#         temp = msvcrt.getche()
#         if temp == '\r':
#             data = ''.join(message)
#             socket.sendall(data.encode('utf-8'))
#             message.clear()
#         else:
#             message.append(temp)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
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
            message = socks.recv(2048)
            print(message.decode('utf-8'))
        else:
            message = sys.stdin.readline()
            server.send(message.encode('utf-8'))
            sys.stdout.write('<You>')
            sys.stdout.write(message)
            sys.stdout.flush()
            # write(socks)

server.close()
