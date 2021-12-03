from pydantic import BaseModel
from typing import Optional


class Category(BaseModel):
    category_id: int
    category_name: str


class CreateCategory(BaseModel):
    category_name: str


class UpdateCategory(BaseModel):
    category_id: int
    category_name: Optional[str]
