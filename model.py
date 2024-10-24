from sqlalchemy import Column, Date, DateTime, Integer,String,Enum
from datetime import datetime

from  .database import Base
from .enums import Gender

class User(Base):
    __tablename__ ="user"

    #basic details
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username =Column(String, unique=True)
    name = Column(String)
    hashed_password = Column(String, nullable=False)
    created_dt = Column(DateTime,default=datetime.utcnow())

    #profile
    dop = Column(Date)
    Gender = Column(Enum(Gender))
    profile_pic = Column(String) #link to our dp
    bio = Column(String)
    location = Column(String)

