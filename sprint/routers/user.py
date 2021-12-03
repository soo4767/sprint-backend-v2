from fastapi import APIRouter, Depends, status, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from sprint.user import schema as user_schema
from sprint.user.service import service_user
from database import get_db

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.post('')
def create(request: user_schema.CreateUser, db: Session = Depends(get_db)):
    return service_user.create(db=db, obj_in=request)


@router.put('')
def update(request: user_schema.UpdateUser, db: Session = Depends(get_db)):
    return service_user.update(db=db, obj_in=request, db_obj=service_user.get(db=db, id=request.user_id))


@router.get('/list')
def get(page: Optional[int] = 0, count: Optional[int] = None, db: Session = Depends(get_db)):
    return service_user.get_multi(db=db, skip=page, limit=count)


@router.get('/{user_id}')
def get_list(user_id: int, db: Session = Depends(get_db)):
    return service_user.get(db=db, id=user_id)


@router.delete('/{user_id}')
def delete(user_id: int, db: Session = Depends(get_db)):
    return service_user.remove(db=db, id=user_id)
