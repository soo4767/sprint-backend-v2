from typing import Union, Dict, Any, List, Optional

from sqlalchemy.orm import Session

from sprint.service.service_base import ServiceBase, ModelType, UpdateSchemaType, CreateSchemaType
from .schema import CreateUser, UpdateUser
from .model import User as UserModel


class ServiceUser(ServiceBase[UserModel, CreateUser, UpdateUser]):

    def get(self, db: Session, id: Any) -> Optional[UserModel]:
        return super().get(db, id)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[UserModel]:
        return super().get_multi(db, skip=skip, limit=limit)

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> UserModel:
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: UserModel, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> UserModel:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def remove(self, db: Session, *, id: int) -> UserModel:
        return super().remove(db, id=id)


service_user = ServiceUser(UserModel)
