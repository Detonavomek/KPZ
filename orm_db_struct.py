#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from sqlalchemy import *
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker

db = create_engine('mysql+mysqldb:///register?charset=utf8')
db.echo = False
metadata = MetaData(db)
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()
Base.metadata.reflect(db)

def session_commit():
    try:    session.commit()
    except:
        session.rollback()
        print 'Commit error!'
    	raise

class Court(Base):  __table__ = Base.metadata.tables['court']
class Removal(Base):    __table__ = Base.metadata.tables['removal']
class CourtMeeting(Base):   __table__ = Base.metadata.tables['court_meeting']
class DisciplinaryAction(Base):   __table__ = Base.metadata.tables['disciplinary_action']
class People(Base):   __table__ = Base.metadata.tables['people']
class Register(Base):   __table__ = Base.metadata.tables['register']
class Registrator(Base):   __table__ = Base.metadata.tables['registrator']
class Statements(Base):   __table__ = Base.metadata.tables['statements']
class StatementsTypes(Base):   __table__ = Base.metadata.tables['statements_types']
class Violance(Base):   __table__ = Base.metadata.tables['violance']