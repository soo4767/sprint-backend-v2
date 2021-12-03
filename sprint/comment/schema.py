from pydantic import BaseModel
from typing import Optional


class Comment(BaseModel):
    comment_id: int
    content: str
    board_id: int
    user_id: int


class CreateComment(BaseModel):
    content: str
    board_id: int
    user_id: int


class UpdateComment(BaseModel):
    comment_id: int
    content: Optional[str]
