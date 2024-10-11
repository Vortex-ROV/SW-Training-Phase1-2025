import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
name = input("Enter name: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'TEST':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print("connection error")
            client.close()
            break

def send():
    while True:
        message = f"{name}: {input('')}"
        client.send(message.encode('utf-8'))

threading.Thread(target=receive).start()
threading.Thread(target=send).start()
