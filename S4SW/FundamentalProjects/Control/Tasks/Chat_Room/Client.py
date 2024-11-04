import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.56.1',55555))

nickname = input("Choose a Nickname: ")

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("an error occurred!")
            client.close()
            break
            raise


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
