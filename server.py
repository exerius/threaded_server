#Многопоточный эхо-сервер
import socket, threading


def echo(connection): #поток для каждого из клиентов
    while True:
        data = connection.recv(1024)
        decoded_data = data.decode()
        if decoded_data != "exit":
            connection.send(data)
        else:
            connection.close()
            break


sock = socket.socket()
sock.bind(("127.0.0.1", 9090))
sock.listen()
conns = []
while True:
    i, addr = sock.accept()
    conns.append(i)
    threading.Thread(target=echo, args=[i]).start() # создаем поток при подключении нового клиента

