import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5001                # Reserve a port for your service.

s.connect((host, port))

print ("This is the message received from the server" , s.recv(1024))
s.close 
