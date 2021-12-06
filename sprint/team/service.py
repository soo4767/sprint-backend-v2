from typing import Union, Dict, Any, List, Optional

from sqlalchemy.orm import Session

from sprint.service.service_base import ServiceBase, ModelType, UpdateSchemaType, CreateSchemaType
from sprint.team.schema import CreateTeam, UpdateTeam, CreateTeamAddUser, InviteTeam
from sprint.team.model import Team as TeamModel
from sprint.user.model import User as UserModel


class ServiceTeam(ServiceBase[TeamModel, CreateTeam, UpdateTeam]):
    def create_with_user_id(self, db: Session, *, obj_in: CreateTeamAddUser) -> TeamModel:
        create_team_schema = obj_in.team
        team = super().create(db, obj_in=create_team_schema)
        user = db.query(UserModel).filter(UserModel.id == obj_in.user_id).first()
        team.user_list.append(user)
        db.commit()
        db.refresh(team)
        return team

    def invite(self, obj_in: InviteTeam, db: Session) -> TeamModel:
        team = super().get(db=db, id=obj_in.id)
        user = db.query(UserModel).get(obj_in.user_id)
        team.user_list.append(user)
        db.commit()
        db.refresh(team)
        return team

    def get(self, db: Session, id: Any) -> Optional[TeamModel]:
        return super().get(db, id)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[TeamModel]:
        return super().get_multi(db, skip=skip, limit=limit)

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> TeamModel:
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: TeamModel, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> TeamModel:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def remove(self, db: Session, *, id: int) -> TeamModel:
        return super().remove(db, id=id)


service_team = ServiceTeam(TeamModel)
