import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
from pkg.models import *

basedir = os.path.abspath(os.path.dirname(__file__))
#sqlite database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'hs.db')

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(engine)
