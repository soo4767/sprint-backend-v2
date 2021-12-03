from database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    team_list = relationship('Team', secondary='team_user_relation', back_populates='user_list')
    board_list = relationship("Board", backref='user')
    comment_list = relationship("Comment", backref='user')
