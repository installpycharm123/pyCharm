import socket               # Import socket module

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Create a socket object

host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
serversocket.bind((host, port))        # Bind to the port

print("server in listen mode")
serversocket.listen(5)                 # Now wait for client connection.
while True:
   clientsocket, addr = serversocket.accept()     # Establish connection with client.
   print("connection has been establihed from :",addr)
   
   clientsocket.send(bytes('Thank you for connecting',"utf-8"))
   clientsocket.close()
                 