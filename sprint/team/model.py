from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    team_name = Column(String)

    category_list = relationship("Category", secondary='team_category_relation', back_populates='team_list')
    user_list = relationship('User', secondary='team_user_relation', back_populates='team_list')
    board_list = relationship('Board', backref='team')


class TeamUserRelation(Base):
    __tablename__ = 'team_user_relation'

    team_id = Column(ForeignKey('team.id', ondelete="CASCADE"), primary_key=True)
    user_id = Column(ForeignKey('user.id', ondelete="CASCADE"), primary_key=True)


class TeamCategoryRelation(Base):
    __tablename__ = 'team_category_relation'

    team_id = Column(ForeignKey('team.id', ondelete="CASCADE"), primary_key=True)
    category_id = Column(ForeignKey('category.id', ondelete="CASCADE"), primary_key=True)
