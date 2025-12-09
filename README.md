# Curse of Networks: Socket Programming (TCP Client-Server MVP)

## 🎯 Project Goal
This project is the Minimum Viable Product (MVP) for a university computer science club initiative focused on understanding network communication fundamentals. It implements a basic, single-threaded TCP Client-Server model using Python's built-in `socket` module.

The primary objective is to demonstrate the **TCP Three-Way Handshake** and reliable data transfer (send/receive) between two separate processes running on the local machine (localhost).

---

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Networking:** TCP/IP Sockets (via Python's `socket` module)
* **Design:** Client-Server Model (Point-to-Point)

---

## 📂 File Structure

# Networking Scripts Overview

## `client.py`
Implements the **client** role:

- Connects to the server  
- Sends data  
- Receives an acknowledgment (ACK)  
- Closes the connection  

## `server.py`
Implements the **server** role:

- Binds to a host and port  
- Listens for incoming connections  
- Accepts a client connection  
- Receives data from the client  
- Sends a response  
- Closes the connection  



---

## 🚀 Getting Started

### Prerequisites

1.  **Python 3.x:** Ensure Python 3 is installed and accessible via your terminal.
    ```bash
    python3 --version
    ```

### Execution Steps

The server **must** be started before the client can attempt a connection. This project is configured for a single, sequential communication session.

1.  **Start the Server (Terminal 1):**
    Open one terminal window and execute the server script. The server will enter a **blocking** state, waiting at the `s.accept()` call.
    ```bash
    python3 server.py
    ```
    *Expected Status: Server outputs "Server initializing..." and pauses.*

2.  **Run the Client (Terminal 2):**
    Open a *second, separate* terminal window and execute the client script.
    ```bash
    python3 client.py
    ```
    *Expected Status: Client connects, sends data, receives acknowledgement, and both client and server processes terminate.*

---

## 💡 Key Design Notes (MVP)
* **Protocol:** Uses TCP (stream sockets) for guaranteed delivery.
* **Host/Port:** Configured for `127.0.0.1:8888` (localhost).
* **Lifecycle:** The `server.py` script is designed to handle **one single client connection** and then shut down immediately, satisfying the initial MVP requirement.
* **Data Handling:** All data is handled as bytes and uses `encode('utf-8')` and `decode('utf-8')` for string readability.