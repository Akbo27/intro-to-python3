import socket
import threading

HOST = '10.237.23.148'
PORT = 21002

def send_message_function(client_socket):
    while True:
        message = input("Enter your message:")
        client_socket.send(((message+"\n").encode()))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")
