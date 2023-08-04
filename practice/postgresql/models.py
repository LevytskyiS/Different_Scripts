from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)
    group_id = Column("group_id", ForeignKey("groups.id", ondelete="CASCADE"))
    group = relationship("Group", backref="students", innerjoin=True)


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
