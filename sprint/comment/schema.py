from pydantic import BaseModel
from typing import Optional


class Comment(BaseModel):
    id: int
    content: str
    board_id: int
    user_id: int


class CreateComment(BaseModel):
    content: str
    board_id: int
    user_id: int


class UpdateComment(BaseModel):
    id: int
    content: Optional[str]
