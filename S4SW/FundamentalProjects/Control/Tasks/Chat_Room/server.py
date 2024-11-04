import threading
import socket

host = '192.168.56.1'
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except: 
            index = clients.index(client)
            clients.remove(index)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            break
            raise

def recieve():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')

        nicknames.append(nickname)
        clients.append(client)

        print(f"nickname of the client: {nickname}")
        broadcast(f'{nickname} joined to the chat!'.encode('ascii'))
        client.send('connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print("Server is Listening....")
recieve()
