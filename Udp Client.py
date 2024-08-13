"""
TITLE - UDP CLIENT SIDE
CODE CONTRIBUTED BY SATYA_AJAY
"""
import socket as skt

client_socket = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
message = input('Enter a Message To Send :')
if message == '':
    message = 'Hello from Ajay!'
ads_tuple = (skt.gethostbyname(skt.gethostname()), 12345)
client_socket.sendto(message.encode('utf-8'), ads_tuple)
