import socket
host=socket.gethostname() #since my same machine is acting as a server as well as client hence I'm using gethostname(), if your server is a remote PC assign the IP address of it as a string to host
port=5000 #same port number as used in server.py
client_socket=socket.socket()
client_socket.connect((host,port))
data=input("->")
while data.lower().strip() != 'bye' :
  client_socket.send(data.encode())
  msg=client_socket.recv(1024).decode()
  print("Received from server: "+str(msg))
  data=input('->')
client_socket.close()
