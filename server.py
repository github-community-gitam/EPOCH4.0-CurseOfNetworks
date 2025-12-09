# server.py
import socket

# --- Configuration Parameters ---
HOST = '127.0.0.1'  # Standard loopback interface address
PORT = 8888         # Listening port

print(f"Server initializing on {HOST}:{PORT}...")

# Initialize TCP socket (AF_INET for IPv4, SOCK_STREAM for TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind socket to the configured address and port
    s.bind((HOST, PORT))
    
    # Configure socket to accept incoming connections (queue size 1)
    s.listen(1) 

    # Primary loop for connection acceptance
    while True:
        # Blocking call: wait until a client connects. Returns new connection socket and client address.
        conn, addr = s.accept()
        
        print(f"\n--- Connection Accepted ---")
        print(f"Client Address: {addr}")
        
        # Handle the client connection
        with conn:
            # Receive data payload (max 1024 bytes)
            data_bytes = conn.recv(1024) 
            
            # Decode received bytes to UTF-8 string
            client_message = data_bytes.decode('utf-8')
            print(f"Received data: '{client_message.strip()}'")

            # Construct response payload
            response_message = f"SERVER ACK: Message received. Data length: {len(client_message.strip())} bytes."
            
            # Encode response string back to bytes for network transmission
            response_bytes = response_message.encode('utf-8')
            
            # Transmit response payload to the client
            conn.sendall(response_bytes)
            
        print("Connection terminated.")
        # MVP requirement: Exit after single client service
        break 

print("Server process exiting.")