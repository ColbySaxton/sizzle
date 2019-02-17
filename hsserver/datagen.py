#!/usr/bin/env python3.6
from pkg import engine
from pkg.models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from datetime import datetime

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

eint1 = Interested_in_Event(1,1)
eint2 = Interested_in_Event(1,2)
eint3 = Interested_in_Event(1,3)
eint4 = Interested_in_Event(2,4)
eint5 = Interested_in_Event(2,5)
for eint in [eint1,eint2,eint3,eint4,eint5]:    
        Session.add(eint)


h1  = Hotspots('h1','h1desc',100,1,1)
h2  = Hotspots('h2','h2desc',-30,-30,1)
Session.add(h1)
Session.add(h2)

hint1 = Interested_in_Hotspot(1,1)
hint2 = Interested_in_Hotspot(1,2)
hint3 = Interested_in_Hotspot(1,3)
hint4 = Interested_in_Hotspot(2,4)
hint5 = Interested_in_Hotspot(2,5)
for hint in [hint1,hint2,hint3,hint4,hint5]:    
        Session.add(hint)
Session.commit()
