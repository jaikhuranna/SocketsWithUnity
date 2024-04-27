import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 12345)
server_socket.bind(server_address)
server_socket.listen(1)
print("Server is running...")

while True:
    connection, client_address = server_socket.accept()
    try:
        print("Connection from", client_address)
        random_number = random.randint(1, 30)
        print("Sending random number:", random_number)
        connection.sendall(str(random_number).encode())
    finally:
        connection.close()
