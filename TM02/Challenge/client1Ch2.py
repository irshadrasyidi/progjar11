import socket
import sys

while True:
    IP = str(input("Enter IP : "))
    port_server = int(input("Enter Port Server : "))

    server_address = (IP, port_server)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    strsend = "Hi...."
    client_socket.send(strsend.encode())

    try:
        while True:
            data = client_socket.recv(1024).decode()
            print(str(data))
            client_socket.close()

            break
    except KeyboardInterrupt:
        client_socket.close()
        sys.exit(0)