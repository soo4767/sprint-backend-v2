from pydantic import BaseModel
from typing import Optional


class Category(BaseModel):
    id: int
    category_name: str

    class Config:
        orm_mode = True


class CreateCategory(BaseModel):
    category_name: str
    team_id: int


class UpdateCategory(BaseModel):
    id: int
    category_name: Optional[str]


class CategoryWithValue(BaseModel):
    id: Optional[int]
    category_name: Optional[str]
    value: Optional[str]

    class Config:
        orm_mode = True
