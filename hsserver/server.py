#!/usr/bin/env python3.6
from pkg import engine
from pkg.models import *
import socket
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, or_, and_, update
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8000
Sessionmaker = sessionmaker(bind=engine)
Session = Sessionmaker()

def getEvents():
        events = (Session.query(Events,func.count(Interested_in_Event.id)).outerjoin(Interested_in_Event).group_by(Events).all())
        #events = Session.query(Events,Interested_in_Event).group_by(Events).all()
        return(events)

def getHotspots():
        hs = (Session.query(Hotspots,func.count(Interested_in_Hotspot.id)).outerjoin(Interested_in_Hotspot).group_by(Hotspots).all())
        #hs = Hotspots.query.all()
        return(hs)

def createUser(email,password_hash):
        u = User(password_hash,email)
        Session.add(u)
        Session.commit()


def updateCounts():
        Session.execute(update(Events, values={Events.trend: Events.recentTally- Events.live_number}))
        Session.execute(update(Events, values={Events.live_number: Events.recentTally}))
        Session.execute(update(Events, values={Events.recentTally: 0}))
        Session.execute(update(Hotspots, values={Hotspots.trend: Hotspots.recentTally- Hotspots.live_number}))
        Session.execute(update(Hotspots, values={Hotspots.live_number: Hotspots.recentTally}))
        Session.execute(update(Hotspots, values={Hotspots.recentTally: 0}))
        Session.commit()
                

def geoTally(u_id,x,y):
        eventNearby = Session.query(Events).filter(and_(and_(x<3+Events.x_coordinate,x>Events.x_coordinate-3),\
                                                        and_(y<3+Events.y_coordinate,y>Events.y_coordinate-3))).one_or_none()
        hsNearby = Session.query(Hotspots).filter(and_(and_(x<3+Hotspots.x_coordinate,x>Hotspots.x_coordinate-3),\
                                                     and_(y<3+Hotspots.y_coordinate,y>Hotspots.y_coordinate-3))).one_or_none()
        if eventNearby is not None:
                eventNearby.recentTally += 1
                Session.add(eventNearby)
        if hsNearby is not None:
                hsNearby.recentTally += 1
                Session.add(hsNearby)
        Session.commit()


def int_in_event(e_id,u_id):
        iie = Interested_in_Event(e_id,u_id)
        Session.add(iie)
        Session.commit()

def int_in_hs(hs_id,u_id):
        iih = Interested_in_Hotspot(hs_id,u_id)
        Session.add(iih)
        Session.commit()
        

'''
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

'''
