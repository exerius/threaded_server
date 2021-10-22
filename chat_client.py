import socket, threading

def listenig():
    while True:
        data = sock.recv(1024)
        print(data.decode())


sock = socket.socket()
sock.connect(("127.0.0.1", 9090))
thread = threading.Thread(target=listenig)
thread.start()
while True:
    message = input()
    sock.send(message.encode())