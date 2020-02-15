import socket
import sys
import os

while True:
    IP = str(input("Enter IP : "))
    port_server = int(input("Enter Port Server : "))
    filename = str(input("Enter File Name : "))
    filesize = os.path.getsize(filename)
    # separate = "\n"

    server_address = (IP, port_server)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    client_socket.send(f"{filename} {filesize}".encode())

    print(client_socket.recv(128).decode())
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(128)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)
            print("packet sent!!!")

    try:
        while True:
            # data = client_socket.recv(1024).decode()
            # print(str(data))
            client_socket.close()
            break

    except KeyboardInterrupt:
        client_socket.close()
        sys.exit(0)