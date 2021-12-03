from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String)

    board_list = relationship("BoardCategoryRelation", back_populates="category")
    team_list = relationship("Team", secondary='team_category_relation', back_populates='category_list')
