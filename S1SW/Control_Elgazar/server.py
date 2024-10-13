import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT = 'DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# List to hold connected clients
clients = []

def broadcast(message, conn):
    """Send message to all clients except the sender"""
    for client in clients:
        if client != conn:
            client.send(message)

def handle_clients(conn, addr):
    """Handle communication with a connected client"""
    print(f"NEW CONNECTION {addr} is connected.")
    clients.append(conn)  # Add client to the list of connected clients
    connected = True
    while connected:
        try:
            msg_len = conn.recv(HEADER).decode(FORMAT).strip()  # Get message length
            if msg_len:
                msg_len = int(msg_len)
                msg = conn.recv(msg_len).decode(FORMAT)  # Receive actual message
                print(f"[{addr}] {msg}")

                if msg == DISCONNECT:
                    connected = False
                else:
                    # Broadcast the message to other clients
                    broadcast(f"[{addr}] {msg}".encode(FORMAT), conn)
        except Exception as e:
            print(f"Error handling client {addr}: {e}")
            connected = False

    conn.close()
    clients.remove(conn)  # Remove the client when disconnected
    print(f"CLIENT {addr} DISCONNECTED")

def start():
    """Start the server and accept new connections"""
    server.listen()
    print(f"SERVER IS LISTENING on {SERVER}")
    while True:
        conn, addr = server.accept()  # Accept new connection
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS: {threading.active_count() - 1}")

print("SERVER IS STARTING")
start()
