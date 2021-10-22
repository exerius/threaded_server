import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 9091))
data = sock.recv(1024).decode()
if data == "Как к вам обращаться?":
    name = input()
    sock.send(name.encode())
else:
    print(data)
sock.close()