from typing import Union, Dict, Any, List, Optional

from sqlalchemy.orm import Session

from sprint.service.service_base import ServiceBase, UpdateSchemaType, CreateSchemaType
from sprint.comment.schema import CreateComment, UpdateComment
from sprint.comment.model import Comment as CommentModel


class ServiceComment(ServiceBase[CommentModel, CreateComment, UpdateComment]):

    def get(self, db: Session, id: Any) -> Optional[CommentModel]:
        return super().get(db, id)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[CommentModel]:
        return super().get_multi(db, skip=skip, limit=limit)

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> CommentModel:
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: CommentModel,
               obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> CommentModel:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def remove(self, db: Session, *, id: int) -> CommentModel:
        return super().remove(db, id=id)


service_comment = ServiceComment(CommentModel)
