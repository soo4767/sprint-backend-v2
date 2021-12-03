from pydantic import BaseModel
from typing import Optional


class Board(BaseModel):
    board_id: int
    board_status: str
    board_content: str
    user_id: int
    team_id: int
    parent_id: int


class CreateBoard(BaseModel):
    board_status: Optional[str]
    board_content: str
    user_id: int
    team_id: int
    parent_id: Optional[int]


class UpdateBoard(BaseModel):
    board_id: int
    board_status: str
    board_content: str
    parent_id: int
