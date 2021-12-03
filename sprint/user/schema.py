from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_id: int
    username: str
    password: str


class CreateUser(BaseModel):
    username: str
    password: str


class UpdateUser(BaseModel):
    user_id: int
    username: Optional[str]
    password: Optional[str]


class ShowUser(BaseModel):
    id: int
    username: str
    team_list: list
    board_list: list
    comment_list: list

    class Config:
        orm_mode = True
