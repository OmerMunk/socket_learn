import socket
import select

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8820


server_socket = socket.socket()

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen()
print(f"Server is up and running on: {SERVER_HOST}:{SERVER_PORT}")


initial_identifier = 6552

CONNECTIONS_LIMIT = 5
client_sockets = []

while True:
    read_list, write_list, error_list = select.select([server_socket], [], [])

    for current_socket in read_list:
        if current_socket == server_socket:
            if len(client_sockets) < CONNECTIONS_LIMIT:
                connection, client_address = server_socket.accept()
                print(f"client joined: {client_address}")
                client_sockets.append({
                    "connection": connection,
                    "client_address": client_address,
                    "id": initial_identifier
                })
                initial_identifier += 1
                print(client_sockets)
            else:
                print("conenction hit the limit")







# data = client_socket.recv(1024).decode()
#
# print("Client sent: " + data)
#
# reply = "Hello " + data
#
# client_socket.send(reply.encode())
#
# client_socket.close()
# server_socket.close()