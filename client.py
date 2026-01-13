# client.py
import socket
import argparse
import sys
from typing import Optional
from datetime import datetime
import time

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8888
TIMEOUT = 5  # seconds
RETRIES = 3  # number of retry attempts if connection fails


def log(message: str):
    """Print a timestamped log message."""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")


def send_message(message: str, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> Optional[str]:
    """Connects to a TCP server, sends a message, and returns the response."""
    attempt = 0
    while attempt < RETRIES:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(TIMEOUT)
                log(f"Connecting to {host}:{port} (Attempt {attempt+1}) ...")
                sock.connect((host, port))
                log("Connection established.")

                sock.sendall(message.encode("utf-8"))
                log(f"Sent → {message}")

                response = sock.recv(1024).decode("utf-8")
                log(f"Received ← {response}")

                return response

        except socket.timeout:
            log("ERROR: Connection attempt timed out.")
        except ConnectionRefusedError:
            log("ERROR: Connection refused — is the server running?")
        except OSError as e:
            log(f"Socket error: {e}")
        except Exception as e:
            log(f"Unexpected error: {e}")

        attempt += 1
        if attempt < RETRIES:
            log("Retrying in 2 seconds...")
            time.sleep(2)

    log("Failed to connect after multiple attempts.")
    return None


def main():
    parser = argparse.ArgumentParser(description="TCP Client to send messages to a server.")
    parser.add_argument("--host", default=DEFAULT_HOST, help="Server IP address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Server port (default: 8888)")
    parser.add_argument("--message", type=str, default="Hello, Server! I am learning about TCP sockets.",
                        help="Message to send to the server")

    args = parser.parse_args()

    try:
        send_message(args.message, args.host, args.port)
    except KeyboardInterrupt:
        log("Client interrupted by user.")
    finally:
        log("Client terminated.")


if __name__ == "__main__":
    main()
