import socket
import threading


def handle_client(sock, addr):
    while True:
        try:
            print('hello')
            sock.sendall(b"\n> ")
            data = sock.recv(1024)

            if not data:
                print(f"Connection closed by {addr}")
                break

            print(f"Received from {addr}: {data.decode()}")
            sock.sendall(data)

        except ConnectionResetError:
            print(f"Connection reset by {addr}")
            break

        except Exception as e:
            print(f"Error with {addr}: {e}")
            break

    print("closing socket")
    sock.close()


def start_server(host: str = "127.0.0.1", port: int = 4444):
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}...")

            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True)
            client_thread.start()

    except KeyboardInterrupt:
        print("Shutting down server...")

    finally:
        server_socket.close()


def main():
    start_server()


if __name__ == "__main__":
    main()
