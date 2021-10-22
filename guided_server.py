import socket, threading


def listening():
    while True:
        known = {}
        try:
            with open("identifications.txt", "r") as file:
                for i in file:
                    line = i.split(":")
                    known.update({line[0]: line[1]})
        except:
            with open("identifications.txt", "w") as file:
                pass
        sock = socket.socket()
        sock.bind(("127.0.0.1", 9091))
        sock.listen(0)
        conn, addr = sock.accept()
        if addr[0] in known:
            conn.send(str(f"Hello,{known[addr[0]]}").encode())
            with open("logs.txt", "w") as file:
                file.write(f"{known[addr[0]]} logged in")
        else:
            conn.send("Как к вам обращаться?".encode())
            data = conn.recv(1024).decode()
            known.update({addr[0]:data})
            with open("identifications.txt", "w") as file:
                for i in known:
                    line = str(i)+":"+str(known[i])
                    file.write(line)
            with open("logs.txt", "w") as file:
                file.write(f"{known[addr[0]]} logged in")
        while True:
            event.wait()
            data = conn.recv(1024)
            decoded = data.decode()
            if decoded == "exit":
                sock.close()
                break
            else:
                conn.send(data)
            event.wait()


event = threading.Event()
event.set()
listen_thread = threading.Thread(target=listening)
#listen_thread = threading.Thread(target=printing)
command =""
listen_thread.start()
while True:
    command = input("Введите команду")
    if command == "quit":
        break
    elif command == "pause":
        event.clear()
    elif command == "resume":
        event.set()
    elif command == "show logs":
        with open("logs.txt", "r") as file:
            for i in file:
                print(i)
    elif command == "clear logs":
        with open("logs.txt", "w") as file:
            file.write("")
    elif command == "clear ids":
        with open("identifications.txt", "w") as file:
            file.write("")
    else:
        print("Нет такой команды")
