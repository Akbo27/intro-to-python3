import socket
import sys
from pyexpat.errors import messages

HOST = '10.237.23.148'
PORT = 21002
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server created")
except OSError as msg:
    s = None
    print(f"Error creating server: {msg}")
    exit(1)

try:
    s.bind((HOST, PORT))
    s.listen()
    print("Server bound and listening")
except OSError as msg:
    print("Error binding/listening!")
    s.close()
    exit(1)

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(32)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode())
            nicknames.remove(nickname)
            break

def receive():
    while True:
        # Accept Connection
        client, address = s.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode())
        nickname = client.recv(32).decode()
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode())
        client.send('Connected to server!'.encode())

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()


