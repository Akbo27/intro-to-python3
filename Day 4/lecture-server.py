import socket
import threading

HOST = '10.237.23.148'
PORT = 21002

class Client:
    def __init__(self, connected_socket, client_id):
        self.connected_socket = connected_socket

clients = []

def send_message_function(client_socket):
    sdf

def boradcast_message(message, author):
    for client in clients:
        if client.client_id != author.client_id:
            try:
                client.connected_socket.send((message+"\n").encode()) 
            except:
                print(f"Sorry, client{client.client_id} looks")
    

def handle_client_communication(client):


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except OSError as msg:
    s = None
    print(f"Error creating socket: {msg}")
    exit(1)

try:
    s.bind((HOST, PORT))
    s.listen()
    print("Socket bound and listening")
except OSError as msg:
    print("Error binding/listening!")
    s.close()
    exit(1)


while True:
    conn, addr = s.accept()
    cli = Client(conn, len(clients))
    clients.append(cli)
    cli_thread = threading.Thread(target=handle_client_communication, args=(cli, ))