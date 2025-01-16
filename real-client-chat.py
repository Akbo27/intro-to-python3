import socket
import threading

HOST = '10.237.23.148'
PORT = 21002

nickname = input("Choose your nickname: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = s.recv(1024).decode('')
            if message == 'NICK':
                s.send(nickname.encode(''))
            else:
                print(message)
        except:
            print("An error occured!")
            s.close()
            break

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        s.send(message.encode())

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()