from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Board(Base):
    __tablename__ = 'board'

    id = Column(Integer, primary_key=True)
    board_status = Column(String)
    board_content = Column(String)

    user_id = Column(ForeignKey('user.id', ondelete="SET NULL"))
    team_id = Column(ForeignKey('team.id', ondelete="CASCADE"))
    parent_id = Column(ForeignKey('board.id', ondelete="SET NULL"))

    category_list = relationship("BoardCategoryRelation", back_populates="board")
    child_list = relationship("Board", remote_side="board.c.id", backref='parent')
    comment_list = relationship("Comment", backref='board')


class BoardCategoryRelation(Base):
    __tablename__ = 'board_category_relation'

    board_id = Column(ForeignKey('board.id', ondelete="CASCADE"), primary_key=True)
    category_id = Column(ForeignKey('category.id', ondelete="CASCADE"))
    value = Column(String)

    category = relationship("Category", back_populates="board_list")
    board = relationship("Board", back_populates="category_list")
