#!/usr/bin/env python3.6
from pkg import engine
import socket
from sqlalchemy.orm import sessionmaker

HOST = "172.19.37.18"
PORT = 8000
Session = sessionmaker(bind=engine)

def getEvents():
        events = (Session.query(Events,func.count(Interested_in_Event.id)).outerjoin(Interested_in_Event).group_by(Events))
        return(events)

print(getEvents())
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			#if not data:
				#break
			conn.sendall(data)


def getHotspots():
	hs = Hotspots.query.all()
	return(hs)

