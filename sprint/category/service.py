from typing import Union, Dict, Any, List, Optional

from sqlalchemy.orm import Session

from sprint.service.service_base import ServiceBase, UpdateSchemaType, CreateSchemaType
from sprint.category.schema import CreateCategory, UpdateCategory
from sprint.category.model import Category as CategoryModel


class ServiceCategory(ServiceBase[CategoryModel, CreateCategory, UpdateCategory]):

    def get(self, db: Session, id: Any) -> Optional[CategoryModel]:
        return super().get(db, id)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[CategoryModel]:
        return super().get_multi(db, skip=skip, limit=limit)

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> CategoryModel:
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: CategoryModel,
               obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> CategoryModel:
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

    def remove(self, db: Session, *, id: int) -> CategoryModel:
        return super().remove(db, id=id)


service_category = ServiceCategory(CategoryModel)
