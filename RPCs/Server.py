from xmlrpc.server import SimpleXMLRPCServer
import logging

# Set up logging to see the requests
logging.basicConfig(level=logging.INFO)

# Define the server and bind it to a specific IP address and port
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is listening on port 8000...")

# Define functions that will be remotely accessible
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Register functions so they are available to clients
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

# Run the server and wait for incoming requests
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server is shutting down...")
    server.server_close()
