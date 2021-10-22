import socket, threading


def echo(connection):
    while True:
        data = connection.recv(1024)
        decoded_data = data.decode()
        if decoded_data != "exit":
            history.append(decoded_data)
            for i in conns:
                i.send(data)
        else:
            connection.close()
            break


sock = socket.socket()
sock.bind(("127.0.0.1", 9090))
sock.listen()
conns = []
known = []
users = []
history = []
try:
    with open("logins.txt", "r") as file:
        for i in file:
            known.append(i.split(":")[0])
            users.append(i.split(":"))
except:
    with open("logins.txt", "w") as file:
        file.write("")

while True:
    i, addr = sock.accept()
    if addr[0] in known:
        i.send("Введите пароль".encode())
        password = i.recv(1024).decode()
        if password == users[known.index(addr[0])][2]:
            i.send(f"Здравствуйте, {users[known.index(addr[0])][1]}".encode())
            conns.append(i)
            threading.Thread(target=echo, args=[i]).start()
        else:
            i.send("Неверный пароль".encode())
    else:
        i.send("Как к вам обращаться?".encode())
        name = i.recv(1024).decode()
        i.send("Введите пароль".encode())
        password = i.recv(1024).decode()
        known.append(addr[0])
        users.append(([addr[0], name, password]))
        with open("logins.txt", "a") as file:
            line = ":".join(users[len(users)-1])
            file.write(line)
        conns.append(i)
        threading.Thread(target=echo, args=[i]).start()
