#creates an SQLalchemy ORM mapping of database tables
from sqlalchemy import Column, Float, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
########################################################################
#creates User class for users table
class User(Base):
    __tablename__="users" 
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(60))
    password_hash = Column(String(60))
    b_owner = Column(Boolean)
    
    def __init__(self, password_hash,email):
        self.password_hash = password_hash
        self.email=email


class Events(Base):
    __tablename__="events"
    id = Column(Integer,autoincrement=True, primary_key=True)
    name=Column(String(40))
    description=Column(String(1000))
    live_number = Column(Integer)
    trend = Column(Integer)
    x_coordinate = Column(Float)
    y_coordinate = Column(Float)
    date = Column(DateTime)
    recentTally = Column(Integer)
    owner = Column(Integer,ForeignKey("users.id"),nullable=False)
    
    def __init__(self,name,description,x,y, date, owner_id):
        self.name=name
        self.description=description
        self.x_coordinate = x
        self.y_coordinate = y
        self.date = date
        self.owner = owner_id
        self.recentTally = 0
        self.live_number = 0
        self.trend = 0

    def __repr__(self):
        return("name : {}\ndescription : {}\nlive num : {}\ntrend : {}\nx : {}\ny : {}\ndate : {}\nrecent tally : {}\nowner : {}".format(self.name,self.description,self.live_number,self.trend,self.x_coordinate,self.y_coordinate,self.date,self.recentTally,self.owner))


class Hotspots(Base):
    __tablename__="hotspots"
    id = Column(Integer,autoincrement=True, primary_key=True)
    name=Column(String(40))
    description=Column(String(1000))
    live_number = Column(Integer)
    trend = Column(Integer)
    x_coordinate = Column(Float)
    y_coordinate = Column(Float)
    recentTally = Column(Integer)
    owner = Column(Integer,ForeignKey("users.id"),nullable=False)
    
    def __init__(self,name,description,x,y, owner_id):
        self.name=name
        self.description=description
        self.owner = owner_id
        self.x_coordinate = x
        self.y_coordinate = y
        self.recentTally = 0
        self.live_number = 0
        self.trend = 0

    def __repr__(self):
        return("name : {}\ndescription : {}\nlive num : {}\ntrend : {}\nx : {}\ny : {}\nrecent tally : {}\nowner : {}".format(self.name,self.description,self.live_number,self.trend,self.x_coordinate,self.y_coordinate,self.recentTally,self.owner))


class Interested_in_Event(Base):
    __tablename__ = "int_in_events"
    id = Column(Integer,autoincrement=True, primary_key=True)
    event_id = Column(Integer,ForeignKey("events.id"),nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    def __init__(self,e_id,u_id):
        self.event_id = e_id
        self.user_id  = u_id

class Interested_in_Hotspot(Base):
    __tablename__ = "int_in_hotspots"
    id = Column(Integer,autoincrement=True, primary_key=True)
    hs_id = Column(Integer,ForeignKey("hotspots.id"),nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    def __init__(self,hs_id,u_id):
        self.hs_id = hs_id
        self.user_id  = u_id




