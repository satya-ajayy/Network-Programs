"""
TITLE - TCP CLIENT SIDE
CODE CONTRIBUTED BY SATYA_AJAY
"""
import socket as skt

client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
client_socket.connect((skt.gethostbyname(skt.gethostname()), 12345))
message = client_socket.recv(1024)
print(message.decode('utf-8'))
client_socket.close()
