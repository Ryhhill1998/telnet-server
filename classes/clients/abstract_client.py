import socket
from abc import ABC, abstractmethod


class AbstractClient(ABC):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        print(f"Starting connection to {self.host}:{self.port}...")

        return s

    @abstractmethod
    def start(self):
        pass
