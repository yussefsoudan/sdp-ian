#!/usr/bin/env python

import socket


TCP_IP = '192.168.105.28'
TCP_PORT = 1025
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("About to connect...")
s.connect((TCP_IP, TCP_PORT))
print("Connected!")
s.send(MESSAGE)
print("Message sent")
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
