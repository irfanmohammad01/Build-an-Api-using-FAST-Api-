from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    role = Column(String, index=True)
    dob = Column(Date, index=True)
    work_location = Column(String, index=True)
    phone_number = Column(String, index=True)
    country = Column(String, index=True)


