#Import the socket module – This allows us to create network connections.
# Set up the server socket to listen for incoming connections.
# Bind the server to a specific IP address and port number.
# Listen for a client connection.
# Send a message to any client that connects.
# Close the connection once the message is sent.


import socket
import platform

#ip and port number
# ServerIp = "127.0.0.1"
# ServerPort = 65000

#create server socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to ip and port
server_socket.bind(("0.0.0.0", 65000))

#Listen for incoming connections 
server_socket.listen()
print("Waiting for client....")

#accept connection
client_socket, client_address = server_socket.accept()
print(f"connection established: {client_address}")

#message
# message = "yooh"
device_name = platform.node()
client_socket.sendall(device_name.encode("utf-8"))

client_socket.close()
server_socket.close()