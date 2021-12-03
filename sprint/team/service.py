from sqlalchemy.orm import Session

from sprint.service.service_base import ServiceBase
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
        team = super().get(db=db, id=obj_in.team_id)
        user = db.query(UserModel).get(obj_in.user_id)
        team.user_list.append(user)
        db.commit()
        db.refresh(team)
        return team


service_team = ServiceTeam(TeamModel)
