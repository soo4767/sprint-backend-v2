from pydantic import BaseModel
from typing import Optional


class Team(BaseModel):
    id: int
    team_name: str


class CreateTeam(BaseModel):
    team_name: str


class UpdateTeam(BaseModel):
    team_id: int
    team_name: Optional[str]


class CreateTeamAddUser(BaseModel):
    team: CreateTeam
    user_id: int


class InviteTeam(BaseModel):
    user_id: int
    team_id: int


class ShowTeam(BaseModel):
    id: int
    team_name: str
    category_list: list
    user_list: list
    board_list: list

    class Config:
        orm_mode = True
