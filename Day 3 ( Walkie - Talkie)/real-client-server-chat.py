import socket
import threading

HOST = '10.237.23.148'
PORT = 21002

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message, sender=None):
    for client in clients:
        if client != sender:  # Avoid sending the message back to the sender
            try:
                client.send(message)
            except Exception as e:
                print(f"Error sending message to a client: {e}")

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            if not message:
                raise ConnectionError("Empty message received; disconnecting client.")
            broadcast(message, sender=client)
        except Exception as e:
            # Removing And Closing Clients
            print(f"Error handling client: {e}")
            if client in clients:
                index = clients.index(client)
                nickname = nicknames[index]
                broadcast(f"{nickname} left!".encode('ascii'))
                clients.remove(client)
                nicknames.remove(nickname)
                client.close()
            break

# Receiving / Listening Function
def receive():
    while True:
        try:
            # Accept Connection
            client, address = server.accept()
            print(f"Connected with {address}")

            # Request And Store Nickname
            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii').strip()

            # Validate nickname
            if not nickname:
                client.send("Invalid nickname. Connection closed.".encode('ascii'))
                client.close()
                continue

            nicknames.append(nickname)
            clients.append(client)

            # Print And Broadcast Nickname
            print(f"Nickname is {nickname}")
            broadcast(f"{nickname} joined!".encode('ascii'))
            client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

        except Exception as e:
            print(f"Error accepting a new client: {e}")

# Run the server
try:
    print("Server is running...")
    receive()
except KeyboardInterrupt:
    print("\nShutting down the server...")
    for client in clients:
        client.close()
    server.close()
    print("Server shut down.")

receive()


