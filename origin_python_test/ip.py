import socket
import os

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)
os.system("pause")