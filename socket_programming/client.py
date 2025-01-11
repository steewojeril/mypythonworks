import socket

# Create a socket object
c = socket.socket()

# Connect to the server on localhost, port 9999
c.connect(('localhost', 9999))

# Prompt the user to enter their name
name = input("Enter your name: ")

# Send the name to the server as bytes (UTF-8 encoding)
c.send(bytes(name, 'utf-8'))

# Close the client connection
c.close()
