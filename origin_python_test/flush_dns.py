import socket
import os

stdout = os.system("ipconfig /flushdns")
print(stdout)
os.system("pause")