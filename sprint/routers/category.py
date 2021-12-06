from fastapi import APIRouter, Depends, status, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from sprint.category import schema as category_schema
from sprint.category.service import service_category
from database import get_db

router = APIRouter(
    prefix='/category',
    tags=['Category']
)


@router.post('')
def create(request: category_schema.CreateCategory, db: Session = Depends(get_db)):
    return service_category.create(db=db, obj_in=request)


@router.put('')
def update(request: category_schema.UpdateCategory, db: Session = Depends(get_db)):
    return service_category.update(db=db, obj_in=request, db_obj=service_category.get(db=db, id=request.id))


@router.get('/list')
def get_list(page: Optional[int] = 0, count: Optional[int] = None, db: Session = Depends(get_db)):
    return service_category.get_multi(db=db, skip=page, limit=count)


@router.get('/{user_id}')
def get(user_id: int, db: Session = Depends(get_db)):
    return service_category.get(db=db, id=user_id)


@router.delete('/{user_id}')
def delete(user_id: int, db: Session = Depends(get_db)):
    return service_category.remove(db=db, id=user_id)
