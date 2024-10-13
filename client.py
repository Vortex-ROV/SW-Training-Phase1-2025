import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Message: {message}")

def send_messages(client_socket):
    while True:
        message = input("")
        client_socket.sendall(message.encode('utf-8'))

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))


    thread_recv = threading.Thread(target=receive_messages, args=(client_socket,))
    thread_send = threading.Thread(target=send_messages, args=(client_socket,))

    thread_recv.start()
    thread_send.start()

if __name__ == "__main__":
    start_client()
