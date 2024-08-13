"""
TITLE - CHAT SERVER SIDE
CODE CONTRIBUTED BY SATYA_AJAY
"""
import socket as skt

HOST_IP = skt.gethostbyname(skt.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

server_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

print('Server Is Running')
client_socket, client_address = server_socket.accept()
client_socket.send('You Are Connected To Server Successfully'.encode(ENCODER))

while True:
    msg = client_socket.recv(1024).decode(ENCODER)
    if msg.title() == 'Quit':
        client_socket.send('Quit'.encode(ENCODER))
        print('Ending The Chat Session Byee')
        break
    else:
        print('CLIENT :', msg)
        msg = input('Message :')
        client_socket.send(msg.encode(ENCODER))

server_socket.close()
