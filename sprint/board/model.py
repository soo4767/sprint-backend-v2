from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, join
from sqlalchemy.orm import relationship, aliased


class Board(Base):
    __tablename__ = 'board'

    id = Column(Integer, primary_key=True)
    board_status = Column(String)
    board_content = Column(String)

    user_id = Column(ForeignKey('user.id', ondelete="SET NULL"))
    team_id = Column(ForeignKey('team.id', ondelete="CASCADE"))
    parent_id = Column(ForeignKey('board.id', ondelete="SET NULL"))

    category_list = relationship("BoardCategoryRelation", back_populates="board")

    parent = relationship("Board", primaryjoin='board.c.id == board.c.parent_id', backref='child_list',
                          remote_side='board.c.id')
    comment_list = relationship("Comment", backref='board')


class BoardCategoryRelation(Base):
    __tablename__ = 'board_category_relation'

    board_id = Column(ForeignKey('board.id', ondelete="CASCADE"), primary_key=True)
    category_id = Column(ForeignKey('category.id', ondelete="CASCADE"), primary_key=True)
    value = Column(String)

    category = relationship("Category", back_populates="board_list")
    board = relationship("Board", back_populates="category_list")

# from sprint.team.model import Team
# from sprint.category.model import Category
#
#
#
# # 1. set up the join() as a variable, so we can refer
# # to it in the mapping multiple times.
# j = join(Team, Category, Category.team_id == Team.id).join(BoardCategoryRelation,
#                                                            BoardCategoryRelation.category_id == Category.id)
#
# # 2. Create an AliasedClass to B
# category_viacd = aliased(BoardCategoryRelation, j, flat=True)
#
# Board.category_list = relationship(category_viacd, primaryjoin=Board.id == j.c.board_id)
