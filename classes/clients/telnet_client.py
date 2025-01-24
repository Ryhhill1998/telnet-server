from classes.clients.abstract_client import AbstractClient


class TelnetClient(AbstractClient):
    def __init__(self, host: str, port: int):
        super().__init__(host=host, port=port)

    def start(self):
        client_socket = self.connect()

        while True:
            data = client_socket.recv(1024)

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

            client_socket.sendall(bytes(msg, encoding="utf-8"))
