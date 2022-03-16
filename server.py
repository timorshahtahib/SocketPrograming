import socket



serverscoket=socket.socket()
serverscoket.bind(socket.gethostbyname,8888)

serverscoket.listen(5)

while True:
    client,add=serverscoket.ac
    print(f"got a coonection from {add}")
    
    msg="thnak you"
    client.send(msg.encode("ascii"))
    client.close()