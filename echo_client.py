import socket

HOST = "127.0.0.1"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)

        if not data:
            print("Connection closed by server...")
            break

        print(data.decode().strip())
        msg = input()

        if msg == "exit":
            break

        s.sendall(bytes(msg, encoding="utf-8"))
