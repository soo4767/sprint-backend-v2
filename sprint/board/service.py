from typing import Union, Dict, Any, List, Optional

from sqlalchemy.orm import Session

from sprint.service.service_base import ServiceBase, UpdateSchemaType, CreateSchemaType
from sprint.board.schema import CreateBoard, UpdateBoard
from sprint.board.model import Board as BoardModel
from sprint.board.model import BoardCategoryRelation


class ServiceBoard(ServiceBase[BoardModel, CreateBoard, UpdateBoard]):

    def get(self, db: Session, id: Any) -> Optional[BoardModel]:
        return super().get(db, id)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[BoardModel]:
        board_list = super().get_multi(db, skip=skip, limit=limit)
        for board in board_list:

            for c in board.category_list:
                c.id = c.category.id
                c.category_name = c.category.category_name

        return board_list

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> BoardModel:
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: BoardModel, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> BoardModel:
        board = super().get(db, obj_in.id)
        for category in obj_in.category_list:
            if category.value.strip() != "":
                result = db.query(BoardCategoryRelation).filter(BoardCategoryRelation.board_id == obj_in.id,
                                                                BoardCategoryRelation.category_id == category.id).update(
                    {'value': category.value}, synchronize_session=False)
                if result == 0:
                    new_category_value = BoardCategoryRelation(
                        board_id=obj_in.id,
                        category_id=category.id,
                        value=category.value
                    )
                    db.add(new_category_value)
            else:
                db.query(BoardCategoryRelation).filter(BoardCategoryRelation.board_id == obj_in.id,
                                                       BoardCategoryRelation.category_id == category.id).delete()

        category_has_value_id_list = []
        category_has_value_list = []

        for c in board.category_list:
            c.id = c.category.id
            c.category_name = c.category.category_name
            category_has_value_id_list.append(c.id)
            category_has_value_list.insert(0, c)

        total_list = []

        for c in board.team.category_list:
            if c.id in category_has_value_id_list:
                total_list.append(category_has_value_list.pop())
            else:
                c.value = None
                total_list.append(c)

        return super().update(db=db, db_obj=board, obj_in=obj_in)

    def remove(self, db: Session, *, id: int) -> BoardModel:
        return super().remove(db, id=id)


service_board = ServiceBoard(BoardModel)
