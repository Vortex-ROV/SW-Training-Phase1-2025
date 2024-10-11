import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen()

clients = {}
def broadcast(message):
    for client in clients:
        client.send(message)

def handleClient(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            name = clients[client]
            broadcast(f"{name} left chat".encode('utf-8'))
            del clients[client]
            client.close()
            break

def startServer():
    while True:
        client, _ = server.accept()
        client.send("TEST".encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        clients[client] = name
        broadcast(f"{name} joined chat".encode('utf-8'))
        thread = threading.Thread(target=handleClient, args=(client,))
        thread.start()

print("Server is running...")
startServer()
