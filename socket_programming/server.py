import socket

# Create a socket object
# socket(socket_family, socket_type, protocol=0)

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET:  IPv4.  SOCK_STREAM: socket will use the TCP 
s = socket.socket() # by default ipv4 and tcp
# Bind the socket to localhost on port 9999
s.bind(('localhost', 9999))

# Listen for up to 3 incoming connections
s.listen(3)

print("Server is waiting for connection...")

while True:
    # Accept an incoming connection. This is a blocking call, meaning the server will wait until a client connects.then only it goes to next line
    c, addr = s.accept()
    
    # Receive data from the client (up to 1024 bytes) and decode it using 'utf-8'
    name = c.recv(1024).decode('utf-8')
    
    # Print information about the connection
    print(f"Connected with {addr}")
    print(f"Welcome {name}!")

    # Close the connection with the client
    c.close()
