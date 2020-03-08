import socket
import sys
import os

BUFFER_SIZE = 128

server_address = ('10.151.254.118', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

sys.stdout.write('>> ')

THIS_DIR = os.listdir('coba')
print(THIS_DIR)

THE_DIR = input()

try:
    for i in THIS_DIR:
        lengkap = THE_DIR + "/" + i
        client_socket.send(THE_DIR.encode())
        filesize = os.path.getsize(lengkap)
        client_socket.send(f"{i} {filesize}".encode())
        print(client_socket.recv(BUFFER_SIZE).decode())
        with open(lengkap, "rb") as openFile:
            while True:
                bytes_read = openFile.read(filesize)
                if not bytes_read:
                    break
                client_socket.sendall(bytes_read)
                print("Packet sent")
    # client_socket.send(message.encode())
    # sys.stdout.write(client_socket.recv(1024).decode())
    # sys.stdout.write('>> ')

except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)