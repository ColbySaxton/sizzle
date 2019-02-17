#!/usr/bin/env python3.6
from pkg import engine
from pkg.models import *
import socket
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8000
Sessionmaker = sessionmaker(bind=engine)
Session = Sessionmaker()

'''
u1 = User('yeet','a@b.c')
Session.add(u1)
e1  = Events('e1','e1desc',1.0,1.0,datetime.now(),1)
e2  = Events('e2','e2desc',-1.0,-1.0,datetime.now(),1)
Session.add(e1)
Session.add(e2)
eint1 = Interested_in_Event(1,1)
eint2 = Interested_in_Event(1,2)
eint3 = Interested_in_Event(1,3)
eint4 = Interested_in_Event(2,4)
eint5 = Interested_in_Event(2,5)
for eint in [eint1,eint2,eint3,eint4,eint5]:    
        Session.add(eint)
Session.commit()
'''

def getEvents():
        events = (Session.query(Events,func.count(Interested_in_Event.id)).outerjoin(Interested_in_Event).group_by(Events).all())
        #events = Session.query(Events,Interested_in_Event).group_by(Events).all()
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

