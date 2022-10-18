# Basic Port Scanner

import sys, socket

server = input("Enter Server IP : ")

for port in range(0,1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex( (server, port) )
    if result == 0:
        print("Port " + str(port) + " Open.")
    sock.close()
