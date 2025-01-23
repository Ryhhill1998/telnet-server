import socket

HOST = "127.0.0.1"
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)

        if not data:
            print("Connection closed by server...")
            break

        decoded_data = data.decode()

        if ">" in decoded_data:
            print(decoded_data, end="")
        else:
            print(decoded_data)

        msg = input()

        if msg == "exit":
            break

        s.sendall(bytes(msg, encoding="utf-8"))
