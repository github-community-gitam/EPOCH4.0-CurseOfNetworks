# server.py
import socket
import argparse
import threading
from typing import Tuple
from datetime import datetime

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8888
BACKLOG = 5       # pending connection queue size
TIMEOUT = 10      # seconds


def log(message: str):
    """Print a timestamped log message."""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")


def handle_client(conn: socket.socket, addr: Tuple[str, int]) -> None:
    """Receive a message from a client and send acknowledgement back."""
    log(f"[+] Client connected: {addr}")

    try:
        data = conn.recv(1024)

        if not data:
            log("[-] No data received. Closing connection.")
            return

        try:
            message = data.decode("utf-8")
        except UnicodeDecodeError:
            message = "<non-utf8 data>"
            log("⚠ Could not decode data as UTF-8.")

        log(f"[>] Message received: {message.strip()}")

        response = f"SERVER ACK: Message received. Data length: {len(message.strip())} bytes."
        conn.sendall(response.encode("utf-8"))
        log("[<] Response sent. Closing connection.")

    except socket.timeout:
        log("⚠ Connection timed out while waiting for data.")
    except OSError as e:
        log(f"⚠ Socket error: {e}")
    finally:
        conn.close()


def start_server(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT, threaded: bool = True) -> None:
    """Starts a TCP server that accepts and handles client connections."""
    log(f"🚀 Starting TCP server on {host}:{port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(BACKLOG)
        log("🟢 Server is running. Waiting for connections... (Ctrl + C to stop)")

        try:
            while True:
                conn, addr = server.accept()
                conn.settimeout(TIMEOUT)

                if threaded:
                    # Handle each client in a separate thread
                    client_thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
                    client_thread.start()
                else:
                    # Handle one client at a time
                    handle_client(conn, addr)

        except KeyboardInterrupt:
            log("🛑 Server shutdown requested. Exiting...")
        except OSError as e:
            log(f"⚠ Server socket error: {e}")

    log("👋 Server stopped.")


def main():
    parser = argparse.ArgumentParser(description="TCP Server to handle client messages.")
    parser.add_argument("--host", default=DEFAULT_HOST, help="Server IP address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Server port (default: 8888)")
    parser.add_argument("--no-thread", action="store_true", help="Disable multi-client threading")

    args = parser.parse_args()
    start_server(args.host, args.port, threaded=not args.no_thread)


if __name__ == "__main__":
    main()

