from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    team_id = Column(ForeignKey('team.id', ondelete="CASCADE"))
    category_name = Column(String)

    board_list = relationship("BoardCategoryRelation", back_populates="category")
    team = relationship("Team", back_populates='category_list')
