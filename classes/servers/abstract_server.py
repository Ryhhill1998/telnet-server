import socket
import threading
from abc import ABC, abstractmethod

from classes.command_processors.abstract_command_processor import AbstractCommandProcessor


class AbstractServer(ABC):
    def __init__(self, host: str, port: int, backlog_size: int, command_processor: AbstractCommandProcessor):
        self.host = host
        self.port = port
        self.backlog_size = backlog_size
        self.command_processor = command_processor

    def create_listener(self):
        server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(self.backlog_size)
        print(f"Listening on {self.host}:{self.port}...")

        return server_socket

    @abstractmethod
    def handle_client(self, sock, addr):
        pass

    def start(self):
        listener = self.create_listener()

        try:
            while True:
                client_socket, client_address = listener.accept()
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
            listener.close()
