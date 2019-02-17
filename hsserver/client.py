#!/usr/bin/env python3.6

import socket

HOST = "172.19.37.18"
PORT = 8000
HOTSPOT = 'N 75 W 876'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(HOTSPOT.encode())
	data = s.recv(1024).decode()

print('Received: {}'.format(data))
