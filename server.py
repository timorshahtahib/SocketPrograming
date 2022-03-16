import socket



serverscoket=socket.socket()
serverscoket.bind((socket.gethostname(),8888))

serverscoket.listen(5)

while True:
    client,add=serverscoket.accept()
    print(f"got a coonection from {add}")
    
    msg="thnak you"
    client.send(msg.encode("ascii"))
    client.close()