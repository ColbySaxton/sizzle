#creates an SQLalchemy ORM mapping of database tables
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
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
    
    def __init__(self, username, password_hash,email):
        self.password_hash = password_hash
        self.email=email


class Events(Base):
    __tablename__="events"
    id = Column(Integer,autoincrement=True, primary_key=True)
    name=Column(String(40))
    description=Column(String(1000))
    live_number = Column(Integer)
    trend = Column(Integer)
    x_coordinate = Column(Integer)
    y_coordinate = Column(Integer)
    date = Column(DateTime)
    owner = Column(Integer,ForeignKey("users.id"),nullable=False)
    
    def __init__(self,name,description,x,y, date, owner_id):
        self.name=name
        self.description=description
        self.x_coordinate = x
        self.y_coordinate = y
        self.date = date
        self.owner = owner_id


class Hotspots(Base):
    __tablename__="hotspots"
    id = Column(Integer,autoincrement=True, primary_key=True)
    name=Column(String(40))
    description=Column(String(1000))
    live_number = Column(Integer)
    trend = Column(Integer)
    x_coordinate = Column(Integer)
    y_coordinate = Column(Integer)
    owner = Column(Integer,ForeignKey("users.id"),nullable=False)
    
    def __init__(self,name,description,x,y, owner_id):
        self.name=name
        self.description=description
        self.owner = owner_id
        self.x_coordinate = x
        self.y_coordinate = y

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
    event_id = Column(Integer,ForeignKey("events.id"),nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    def __init__(self,e_id,u_id):
        self.event_id = e_id
        self.user_id  = u_id




