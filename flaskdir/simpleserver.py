import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 5001                
	# Bind to port.
s.bind((host, port))        


#stay in a loop, listening to connections from the client.

s.listen(5)
while True:

   # Listen to any incoming connections.
   c, addr = s.accept()
   
   # now that we have a connection from the client, send message to client.
   print ('Got connection from', addr )
   message = "Sending Hello Message from Server to Python Client "  # str
   binary_message = message.encode('utf-8')
   print(type(binary_message))  # bytes

   c.send(binary_message)
   c.close()
