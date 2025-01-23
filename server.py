import socket
import threading


class Server:
    def __init__(self, host: str, port: int, backlog_size: int):
        self.host = host
        self.port = port
        self.backlog_size = backlog_size

    def start_server(self):
        server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(self.backlog_size)
        print(f"Listening on {self.host}:{self.port}...")

        try:
            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Accepted connection from {client_address}...")

                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, client_address),
                    daemon=True
                )
                client_thread.start()

        except KeyboardInterrupt:
            print("Shutting down server...")

        finally:
            server_socket.close()

    @staticmethod
    def handle_client(sock, addr):
        sock.sendall(b"Connected to echo server...")

        while True:
            try:
                sock.sendall(b">")
                data = sock.recv(1024)

                if not data:
                    print(f"Connection closed by {addr}")
                    break

                print(f"Received from {addr}: {data.decode().strip()}")
                sock.send(data)

            except ConnectionResetError:
                print(f"Connection reset by {addr}")
                break

            except Exception as e:
                print(f"Error with {addr}: {e}")
                break

        print("closing socket")
        sock.close()
