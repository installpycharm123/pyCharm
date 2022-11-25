import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print("connection request is sent")

msg=(s.recv(1024))
print(msg.decode("utf-8"))
s.close()  