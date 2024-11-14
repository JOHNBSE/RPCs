import xmlrpc.client

# Connect to the server
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call the remote functions
print("Add: 10 + 5 =", server.add(10, 5))
print("Subtract: 10 - 5 =", server.subtract(10, 5))
print("Multiply: 10 * 5 =", server.multiply(10, 5))
print("Divide: 10 / 5 =", server.divide(10, 5))

# Handling division by zero
print("Divide: 10 / 0 =", server.divide(10, 0))
