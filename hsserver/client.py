#!/usr/bin/env python3.6

import socket
import json
HOST = "127.0.0.1"
PORT = 8000
HOTSPOT = json.dumps({'getevents':0})

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(HOTSPOT.encode())
	data = s.recv(1024*8)
	print(data.decode())

