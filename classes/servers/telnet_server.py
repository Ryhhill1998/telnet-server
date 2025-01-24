import os

from classes.servers.abstract_server import AbstractServer
from classes.command_processors.telnet_command_processor import TelnetCommandProcessor


class TelnetServer(AbstractServer):

    def __init__(self, host: str, port: int, backlog_size: int, command_processor: TelnetCommandProcessor):
        super().__init__(host=host, port=port, backlog_size=backlog_size, command_processor=command_processor)

    def handle_client(self, sock, addr):
        sock.sendall(b"\n> ")

        while True:
            try:
                data = sock.recv(1024)

                if not data:
                    print(f"Connection closed by {addr}")
                    break

                decoded_data = data.decode("utf-8")
                print(f"Received from {addr}: {decoded_data}")
                res = self.command_processor.process(decoded_data)
                sock.send(bytes(f"{res}\n> ", encoding="utf-8"))

            except ConnectionResetError:
                print(f"Connection reset by {addr}")
                break

            except Exception as e:
                print(f"Error with {addr}: {e}")
                break

        print(f"closing connection to {addr}...")
        sock.close()
