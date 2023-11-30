import socket

# Define host and port
host = '127.0.0.1'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections (max 5 connections in the queue)
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

# Simple firewall rule (allow connections only from localhost)
allowed_addresses = ['127.0.0.1']

while True:
    # Wait for a connection from a client
    client_socket, addr = server_socket.accept()

    # Check if the client's address is allowed
    if addr[0] not in allowed_addresses:
        print(f"Connection from {addr} rejected (firewall rule).")
        client_socket.close()
        continue

    print(f"Connection from {addr}")

    # Send a welcome message to the client
    message = "Welcome to the server!"
    client_socket.send(message.encode())

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print(f"Received data: {data}")

    # Close the connection with the client
    client_socket.close()
