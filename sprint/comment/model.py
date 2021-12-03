from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(String)

    user_id = Column(ForeignKey('user.id', ondelete="SET NULL"))
    board_id = Column(ForeignKey('board.id', ondelete="CASCADE"))
