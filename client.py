#Клиент эхо-сервера
import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 9091))
while True:
        line = input("Введите сообщение")
        sock.send(line.encode())
        message = sock.recv(1024)
        print(message.decode())
