#!/usr/bin/env python3.6
from pkg import engine
from pkg.models import *
import socket
import sched, time
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, or_, and_, update
from datetime import datetime,timedelta
setup_mode = False

HOST = "127.0.0.1"
PORT = 8000
updateTime = 10*60
Sessionmaker = sessionmaker(bind=engine)
Session = Sessionmaker()
updateClient = sched.scheduler(time.time, time.sleep)
lastUpdateTime = datetime.now()
def getEvents():
	events = (Session.query(Events,func.count(Interested_in_Event.id)).outerjoin(Interested_in_Event).group_by(Events).all())
	for i in range(len(events)):
                print(events[i])
                dict = events[i][0].__dict__
                dict.update({'intin':events[i][1]})
                dict.pop('_sa_instance_state',None)
                events[i] = dict
        #events = Session.query(Events,Interested_in_Event).group_by(Events).all()
	return(events)

def getHotspots():
	hs = (Session.query(Hotspots,func.count(Interested_in_Hotspot.id)).outerjoin(Interested_in_Hotspot).group_by(Hotspots).all())	
	for i in range(len(hs)):
		print(hs[i])
		dict = hs[i][0].__dict__
		dict.update({'intin':hs[i][1]})
		dict.pop('_sa_instance_state',None)
		hs[i] = dict
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

if not setup_mode:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		print(HOST)
		print(PORT)
		while True:
			if(lastUpdateTime+timedelta(0,updateTime)<datetime.now()):
				print('updating counts')
				updateCounts()
				lastUpdateTime = datetime.now()
			conn, addr = s.accept()
			with conn:
				if(True):
					print('Connected by', addr)
					client_request = conn.recv(1024).decode()
					js = json.loads(client_request)
					header = list(js.keys())[0]
					print(header)
					response = "{}"
					if(header == 'geths'):
						response = getHotspots()
					elif(header == 'getevents'):
						response = getEvents()
					response = json.dumps(response,default=str)
					conn.sendall(response.encode())
				#except:
					#pass
