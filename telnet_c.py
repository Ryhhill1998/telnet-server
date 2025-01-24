from classes.clients.telnet_client import TelnetClient


def main(host: str, port: int):
    client = TelnetClient(host=host, port=port)
    client.start()


if __name__ == "__main__":
    main(host="127.0.0.1", port=4444)
