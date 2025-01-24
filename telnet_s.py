from classes.command_processors.telnet_command_processor import TelnetCommandProcessor
from classes.servers.telnet_server import TelnetServer


def main(host: str, port: int):
    command_processor = TelnetCommandProcessor()

    server = TelnetServer(host=host, port=port, backlog_size=5, command_processor=command_processor)
    server.start()


if __name__ == "__main__":
    main(host="127.0.0.1", port=4444)
