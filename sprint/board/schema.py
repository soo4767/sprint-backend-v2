from pydantic import BaseModel
from typing import Optional, List, Dict
from sprint.category.schema import CategoryWithValue


class Board(BaseModel):
    id: int
    board_status: str
    board_content: str
    user_id: int
    team_id: int
    parent_id: int

    class Config:
        orm_mode = True


class CreateBoard(BaseModel):
    board_status: Optional[str]
    board_content: str
    user_id: int
    team_id: int
    parent_id: Optional[int]


class UpdateBoard(BaseModel):
    id: int
    board_status: Optional[str]
    board_content: Optional[str]
    parent_id: Optional[int]
    category_list: Optional[List[CategoryWithValue]] = []


class ShowBoard(BaseModel):
    id: int
    board_status: Optional[str]
    board_content: str
    user_id: int
    team_id: int
    parent_id: Optional[int]

    class Config:
        orm_mode = True


class ShowBoardWithParent(BaseModel):
    id: Optional[int]
    board_status: str = None
    board_content: str = None
    user_id: Optional[int]
    team_id: Optional[int]
    parent_id: Optional[int]

    category_list: list = []
    comment_list: list = []
    parent: Board = None

    class Config:
        orm_mode = True


class ShowBoardWithChildren(BaseModel):
    id: Optional[int]
    board_status: str = None
    board_content: str = None
    user_id: Optional[int]
    team_id: Optional[int]
    parent_id: Optional[int]

    category_list: Optional[List[CategoryWithValue]] = []
    comment_list: list = []
    child_list: Optional[List["ShowBoardWithChildren"]]

    class Config:
        orm_mode = True


# Self-Referencing Models :
# https://pydantic-docs.helpmanual.io/usage/postponed_annotations/#:~:text=Self%2Dreferencing%20Models-,%F0%9F%94%97,-Data%20structures%20with
ShowBoardWithChildren.update_forward_refs()


class UpdateBoardCategoryValue(BaseModel):
    board_id: int
    category_id: int
    value: str
