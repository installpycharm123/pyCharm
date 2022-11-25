import socket
table={
'192.168.1.1':'1E.4A.4A.11',
'192.168.2.1':'1E.4B.4C.21',
'192.168.3.2':'CE.C5.FC.F1',
'1E.4A.4A.11':'192.168.1.1',
'1E.4B.4C. 21':'192.168.2.1',
'CE.C5.FC.F1':'192.168.3.2'
}
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1234))
s.listen()
clientsocket,address=s.accept()
print("connection from",address,"Has Established")
ip=clientsocket.recv(1024)
ip=ip.decode("utf-8")
mac=table.get(ip,'no entry for given address')
clientsocket.send(mac.encode())