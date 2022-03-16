import socket



clientsocket=socket.socket()
clientsocket.connect((socket.gethostname(),8888))

msg=clientsocket.recv(2048)
clientsocket.close()
print(msg)
