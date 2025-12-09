# 💡 Contribution Guidelines

This project, "Curse of Networks," serves as a foundation for learning TCP socket programming. Contributions are highly encouraged to expand the server's capabilities and introduce new network concepts.

## 🎯 Feature Expansion Roadmap

The current project is a simple Minimum Viable Product (MVP) that handles one client connection and then shuts down. Future contributions should focus on one of the following architectural tracks.

### Track 1: Persistent Server (Sequential Handling)

**Goal:** Modify `server.py` to handle multiple clients *sequentially* (one after the other) without shutting down.

| Feature Suggestion | Implementation Focus | Details |
| :--- | :--- | :--- |
| **Continuous Listener** | Server Loop | Modify the main `while True:` loop in `server.py` to prevent the `break` statement after a client disconnects. |
| **Connection Reset** | Client Connection Handling | Update the output to clearly indicate when a client connects and when they disconnect, showing the server's readiness for the next connection. |
| **Graceful Shutdown** | User Input Handling | Add logic to the server (e.g., watching for an 'exit' command or a keyboard interrupt like `Ctrl+C`) to terminate the loop cleanly. |

### Track 2: Concurrent Server (Multi-threaded Handling)

**Goal:** Modify `server.py` to handle multiple clients *simultaneously* using threading. This allows the server to continue accepting new connections while actively communicating with existing ones. 

[Image of Multi-Threaded Server Model]


| Feature Suggestion | Implementation Focus | Details |
| :--- | :--- | :--- |
| **Thread Spawning** | `threading` Module | After `s.accept()` returns `conn` and `addr`, immediately spawn a new thread (e.g., using `threading.Thread`) to handle all subsequent communication with that client. |
| **Thread Function** | Connection Handler | Create a dedicated function (e.g., `handle_client(conn, addr)`) where the current data exchange logic resides, allowing the main thread to immediately return to `s.listen()` and `s.accept()`. |
| **Resource Safety** | Thread Synchronization | Consider how multiple threads might affect shared resources (though not critical for this simple MVP, it's a good practice to consider). |

### Track 3: Application Protocol Layer

**Goal:** Introduce basic logic to handle more complex data transfer, overcoming limitations like the fixed `1024` byte buffer.

| Feature Suggestion | Implementation Focus | Details |
| :--- | :--- | :--- |
| **Fixed-Length Header** | Send/Receive Logic | Prepend a short, fixed-length header (e.g., 4 bytes) to every message indicating the total length of the payload that follows. |
| **Looping Receive** | `client.py` and `server.py` | Implement a `while` loop around the `conn.recv()` calls to ensure *all* expected bytes (as indicated by the header) are received, even if they arrive in multiple network packets. |

## ⚙️ How to Contribute

1.  **Fork** the repository.
2.  **Clone** your forked repository locally.
3.  Create a descriptive **branch** for your feature (e.g., `feat/threaded-server`).
4.  Commit your changes, ensuring commit messages are clear and follow a standard convention (e.g., `feat: implement continuous server loop`).
5.  **Push** your branch and open a **Pull Request** targeting the main branch.