**client**
import socket
hostname=socket.gethostname()
ipaddr="127.0.0.1"
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=(ipaddr,1234)
c="Y"
while c.upper()=="Y":
req_domain = input("enter domain name for which the ip is
needed:")
send=s.sendto(req_domain.encode(),addr)
data, address=s.recvfrom(1024)
reply_ip = data.decode().strip()
print(f"the ip for the domain name{req_domain}:{reply_ip}")
c=(input("continue?(y/n)"))
s.close()
**SERVER**
import socket
dns_table={"www.google.com": "192.165.1.1","www.youtube.com":
"192.165.1.2","www.gmail.com": "192.165.1.3"}
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("starting server....")
s.bind(("127.0.0.1",1234))
while True:
data,address=s.recvfrom(1024)
print(f"{address} wants to fetch data")
data=data.decode()
ip=dns_table.get(data,"not found").encode()
send=s.sendto(ip,address)
s.close()