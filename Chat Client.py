"""
TITLE - CHAT CLIENT SIDE
CODE CONTRIBUTED BY SATYA_AJAY
"""
import socket as skt

DEST_IP = skt.gethostbyname(skt.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

while True:
    msg = client_socket.recv(BYTESIZE).decode(ENCODER)
    if msg.title() == 'Quit':
        client_socket.send('Quit'.encode(ENCODER))
        print('Ending The Chat Session Bye')
        break
    else:
        print('SERVER :', msg)
        msg = input('Message :')
        client_socket.send(msg.encode(ENCODER))

client_socket.close()
