#!/usr/bin/env python3.6
from pkg import engine
from pkg.models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from datetime import datetime
from server import *

Sessionmaker = sessionmaker(bind=engine)
Session = Sessionmaker()
#data generator


u1 = User('yeet','a@b.c')
for i in range(50):
    u = User('u{}'.format(i),'u{}'.format(i))
    Session.add(u)

Session.add(u1)
e1  = Events('e1','e1desc',16.0,16.0,datetime.now(),1)
e2  = Events('e2','e2desc',-1.0,-1.0,datetime.now(),1)
Session.add(e1)
Session.add(e2)

int_in_event(1,1)
int_in_event(1,2)
int_in_event(1,3)
int_in_event(2,4)
int_in_event(2,5)


h1  = Hotspots('h1','h1desc',100,1,1)
h2  = Hotspots('h2','h2desc',-30,-30,1)
Session.add(h1)
Session.add(h2)

int_in_hs(1,1)
int_in_hs(1,2)
int_in_hs(1,3)
int_in_hs(2,4)
int_in_hs(2,5)
Session.commit()
