#TCP/IP is a connection oriented protocol and it is byte oriented
import socket
host=socket.gethostname()
port=5000 #any port no above 1024
server_socket=socket.socket()
server_socket.bind((host,port))
server_socket.listen(2) #how many clients server can listen at a time
print("Waiting for incoming connection...")
conn,addr=server_socket.accept()
print("Connection from: "+str(addr))
while True:
  msg=conn.recv(1024).decode()
  if not msg:
    break
  print("From connected user: "+str(msg))
  data=input("->")
  conn.send(data.encode())
conn.close()
