"""
TITLE - UDP SERVER SIDE
CODE CONTRIBUTED BY SATYA_AJAY
"""
import socket as skt

server_socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
server_socket.bind((skt.gethostbyname(skt.gethostname()), 12345))

msg, ads = server_socket.recvfrom(1024)
print(msg.decode('utf-8'))
print(ads)
