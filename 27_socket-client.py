import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# Connect to the server using the port
s.connect(('127.0.0.1', port))

# Send a message to the server
message = "Hello from the client!"
s.send(message.encode())

# Receive data from the server
data = s.recv(1024)
print("Received from the server:", data.decode())

# Close the connection
s.close()
