import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(75), nullable=False)
    username = Column(String(25), nullable=False)
    password = Column(String(25), nullable=False)
    email = Column(String(250), nullable=False)

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(30), nullable=False)
    biography = Column(String(200))


class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(String(25), ForeignKey('user.id'))
    user_to_id = Column(String(25), ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(25), ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    post_id = Column(String, ForeignKey('user.id'))
    user = relationship(User)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text_comment = Column(String(144), ForeignKey('user.id'))
    author_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e