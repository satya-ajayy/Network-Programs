"""
TITLE - TCP SERVER SIDE
CODE CONTRIBUTED BY SATYA_AJAY
"""
import socket as skt

server_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
print(skt.gethostname())
print(skt.gethostbyname(skt.gethostname()))
server_socket.bind((skt.gethostbyname(skt.gethostname()), 12345))
server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    print('Socket  :', client_socket)
    # print(type(client_socket))
    print('Address :', client_address)
    # print(type(client_address))
    print(f'Connected to {client_address}')
    client_socket.send('You Are Connected'.encode('utf-8'))
    server_socket.close()
    break
