import socket
import select
import sys
import threading
import os
import time

BUFFER_SIZE = 2048

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = '192.168.0.103'
port = 8081
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []


def clientthread(conn, addr):
    while True:
        try:
            # print("coba")
            message = conn.recv(BUFFER_SIZE).decode()
            if str(message):
                filename, filesize = message.split()
                print(filename, filesize)
                conn.send("Ok".encode())
                data = conn.recv(int(filesize))
                print('<' + addr[0] + '> ' + "sending")
                broadcast(data, conn, filename, filesize)
            else:
                remove(conn)
        except:
            continue


def broadcast(message, connection, filename, filesize):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(f"{filename} {filesize}".encode('utf-8'))
                time.sleep(2)
                # print(clients.recv(BUFFER_SIZE).decode('utf-8'))
                clients.sendall(message)
            except:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

conn = None
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + ' connected')
    threading.Thread(target=clientthread, args=(conn, addr)).start()
    # print("coba")

conn.close()
