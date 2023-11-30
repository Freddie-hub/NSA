import socket

# Define host and port
host = '127.0.0.1'
port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Receive the welcome message from the server
welcome_message = client_socket.recv(1024).decode()
print(welcome_message)

# Send data to the server
message_to_server = "Hello, server!"
client_socket.send(message_to_server.encode())

# Close the connection with the server
client_socket.close()
