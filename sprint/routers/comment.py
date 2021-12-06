from fastapi import APIRouter, Depends, status, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from sprint.comment import schema as comment_schema
from sprint.comment.service import service_comment
from database import get_db

router = APIRouter(
    prefix='/comment',
    tags=['Comment']
)


@router.post('')
def create(request: comment_schema.CreateComment, db: Session = Depends(get_db)):
    return service_comment.create_with_user_id(db=db, obj_in=request)


@router.put('')
def update(request: comment_schema.UpdateComment, db: Session = Depends(get_db)):
    return service_comment.update(db=db, obj_in=request, db_obj=service_comment.get(db=db, id=request.id))


@router.get('/list')
def get_list(page: Optional[int] = 0, count: Optional[int] = None, db: Session = Depends(get_db)):
    return service_comment.get_multi(db=db, skip=page, limit=count)


@router.get('/{comment_id}')
def get(comment_id: int, db: Session = Depends(get_db)):
    return service_comment.get(db=db, id=comment_id)


@router.delete('/{comment_id}')
def delete(comment_id: int, db: Session = Depends(get_db)):
    return service_comment.remove(db=db, id=comment_id)
