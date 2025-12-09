# client.py
import socket

# --- Configuration Parameters ---
HOST = '127.0.0.1' 
PORT = 8888       

# Initialize TCP socket (AF_INET for IPv4, SOCK_STREAM for TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Attempting connection to {HOST}:{PORT}...")
    
    try:
        # Establish connection to the remote server host and port
        s.connect((HOST, PORT))
        print("Connection established.")

        # Define data payload
        message_to_send = "Hello, Server! I am learning about TCP sockets."
        
        # Encode string to bytes for network transmission
        data_to_send = message_to_send.encode('utf-8')

        # Send all data to the server
        s.sendall(data_to_send)
        print(f"Transmitted: '{message_to_send}'")

        # Receive server response (max 1024 bytes)
        server_response_bytes = s.recv(1024) 

        # Decode received bytes to UTF-8 string
        server_response = server_response_bytes.decode('utf-8')
        print(f"\nReceived from Server: '{server_response}'")
        
    except ConnectionRefusedError:
        # Handle connection failure if server is not listening
        print("\nERROR: Connection refused. Verify the server is running on the specified host and port.")
        
print("Client process exiting.")