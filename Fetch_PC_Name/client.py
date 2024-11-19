# Import the socket module.
# Create a client socket.
# Connect to the server by specifying the server IP and port.
# Receive the message from the server.
# Close the connection once the message is received.

import socket

#server ip and port
# ServerIp = "127.0.0.1"
# ServerPort = 65000

#create a client socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server
client_socket.connect(("172.29.17.119", 65000))

#Receive message from the server
message = client_socket.recv(1024)
print("Message:",message.decode('utf-8'))

#close the connection
client_socket.close()



