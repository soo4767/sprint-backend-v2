from fastapi import APIRouter, Depends, status, HTTPException
from typing import Optional, List
from sqlalchemy.orm import Session
from sprint.board import schema as board_schema
from sprint.board.service import service_board
from database import get_db

router = APIRouter(
    prefix='/board',
    tags=['Board']
)


@router.post('')
def create(request: board_schema.CreateBoard, db: Session = Depends(get_db)):
    return service_board.create(db=db, obj_in=request)


@router.put('', response_model=board_schema.ShowBoardWithChildren)
def update(request: board_schema.UpdateBoard, db: Session = Depends(get_db)):
    return service_board.update(db=db, obj_in=request, db_obj=service_board.get(db=db, id=request.id))


@router.get('/list', response_model=List[board_schema.ShowBoardWithChildren])
def get_list(page: Optional[int] = 0, count: Optional[int] = None, db: Session = Depends(get_db)):
    return service_board.get_multi(db=db, skip=page, limit=count)


@router.get('/{board_id}', response_model=board_schema.ShowBoardWithChildren)
def get(board_id: int, db: Session = Depends(get_db)):
    return service_board.get(db=db, id=board_id)


@router.delete('/{board_id}')
def delete(board_id: int, db: Session = Depends(get_db)):
    return service_board.remove(db=db, id=board_id)
