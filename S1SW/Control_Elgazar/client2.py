import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT = 'DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive_messages():
    """Thread to receive messages from the server"""
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)
            print(msg)  # Print any received message
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_message(msg):
    """Send a message to the server"""
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)

# Start a thread to continuously receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main loop to send messages
while True:
    msg = input()  # Get user input
    if msg == DISCONNECT:
        send_message(DISCONNECT)
        break
    send_message(msg)
