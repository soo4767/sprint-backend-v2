from fastapi import APIRouter, Depends, status, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from sprint.team import schema as team_schema
from sprint.team.service import service_team
from database import get_db

router = APIRouter(
    prefix='/team',
    tags=['Team']
)


@router.post('')
def create(request: team_schema.CreateTeamAddUser, db: Session = Depends(get_db)):
    return service_team.create_with_user_id(db=db, obj_in=request)


@router.put('')
def update(request: team_schema.UpdateTeam, db: Session = Depends(get_db)):
    return service_team.update(db=db, obj_in=request, db_obj=service_team.get(db=db, id=request.team_id))


@router.post('/invite', response_model=team_schema.ShowTeam)
def invite(request: team_schema.InviteTeam, db: Session = Depends(get_db)):
    return service_team.invite(db=db, obj_in=request)


@router.get('/list')
def get(page: Optional[int] = 0, count: Optional[int] = None, db: Session = Depends(get_db)):
    return service_team.get_multi(db=db, skip=page, limit=count)


@router.get('/{team_id}', response_model=team_schema.ShowTeam)
def get_list(team_id: int, db: Session = Depends(get_db)):
    return service_team.get(db=db, id=team_id)


@router.delete('/{team_id}')
def delete(team_id: int, db: Session = Depends(get_db)):
    return service_team.remove(db=db, id=team_id)
