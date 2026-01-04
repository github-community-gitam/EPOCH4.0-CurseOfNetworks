# client.py
import socket
import sys
from typing import Optional

HOST = "127.0.0.1"
PORT = 8888
TIMEOUT = 5  # seconds


def send_message(message: str, host: str = HOST, port: int = PORT) -> Optional[str]:
    """Connects to a TCP server, sends a message, and returns the response."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)

            print(f"Connecting to {host}:{port} ...")
            sock.connect((host, port))
            print("Connection established.")

            sock.sendall(message.encode("utf-8"))
            print(f"Sent → {message}")

            response = sock.recv(1024).decode("utf-8")
            print(f"Received ← {response}")

            return response

    except socket.timeout:
        print("ERROR: Connection attempt timed out.")
    except ConnectionRefusedError:
        print("ERROR: Connection refused — is the server running?")
    except OSError as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


if __name__ == "__main__":
    message = "Hello, Server! I am learning about TCP sockets."

    # Optional: allow host/port overrides from command-line
    if len(sys.argv) >= 2:
        HOST = sys.argv[1]
    if len(sys.argv) >= 3:
        PORT = int(sys.argv[2])

    send_message(message, HOST, PORT)

    print("Client terminated.")
