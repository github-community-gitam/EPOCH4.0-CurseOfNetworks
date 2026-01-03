# server.py
import socket
from typing import Tuple

HOST = "127.0.0.1"
PORT = 8888
BACKLOG = 5       # pending connection queue size
TIMEOUT = 10      # seconds


def handle_client(conn: socket.socket, addr: Tuple[str, int]) -> None:
    """Receive a message from a client and send acknowledgement back."""
    print(f"\n[+] Client connected: {addr}")

    try:
        data = conn.recv(1024)

        if not data:
            print("[-] No data received. Closing connection.")
            return

        try:
            message = data.decode("utf-8")
        except UnicodeDecodeError:
            message = "<non-utf8 data>"
            print("⚠ Could not decode data as UTF-8.")

        print(f"[>] Message received: {message.strip()}")

        response = f"SERVER ACK: Message received. Data length: {len(message.strip())} bytes."
        conn.sendall(response.encode("utf-8"))

        print("[<] Response sent. Closing connection.")

    except socket.timeout:
        print("⚠ Connection timed out while waiting for data.")
    except OSError as e:
        print(f"⚠ Socket error: {e}")
    finally:
        conn.close()


def start_server(host: str = HOST, port: int = PORT) -> None:
    """Starts a TCP server that accepts and handles client connections."""

    print(f"🚀 Starting TCP server on {host}:{port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(BACKLOG)
        server.settimeout(None)

        print("🟢 Server is running. Waiting for connections... (Ctrl + C to stop)")

        try:
            while True:
                conn, addr = server.accept()
                conn.settimeout(TIMEOUT)
                handle_client(conn, addr)

        except KeyboardInterrupt:
            print("\n🛑 Server shutdown requested. Exiting...")
        except OSError as e:
            print(f"⚠ Server socket error: {e}")

    print("👋 Server stopped.")


if __name__ == "__main__":
    start_server()
