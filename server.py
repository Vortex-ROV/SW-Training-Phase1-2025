import socket
import threading

clients = []

def handle_client(conn, addr):
    print(f"{addr} connected.")    #print the address of connected client
    clients.append(conn)
    while True:
        message = conn.recv(1024).decode('utf-8')
        if message:
            broadcast(message, conn)

def broadcast(message, conn):

    for client in clients:
        if client != conn:
            client.sendall(message.encode('utf-8'))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 9999))
    server_socket.listen()

    print("Server started and listening on 127.0.0.1:9999")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
