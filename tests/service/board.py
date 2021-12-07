from tests.base import BaseTest

from sprint.board.service import service_board

from sprint.board.schema import CreateBoard, UpdateBoard, CategoryWithValue
from sprint.user.service import service_user
from sprint.team.service import service_team


class Order_03_Service_Board(BaseTest):
    def setUp(self):
        self.user_list = service_user.get_multi(db=self.db)
        self.team_list = service_team.get_multi(db=self.db)
        self.board_list = service_board.get_multi(db=self.db)
        self.create_board = CreateBoard(
            board_status="status_1",
            board_content="content_1",
            user_id=self.user_list[-1].id,
            team_id=self.team_list[-1].id,
            parent_id=self.board_list[-1].id
        )

    def test_01_create_board(self):
        created_board = service_board.create(db=self.db, obj_in=self.create_board)
        self.assertEqual(created_board.board_content, self.create_board.board_content, msg="test_01_create_board Error")

    def test_02_get_all_board(self):
        board_list = service_board.get_multi(db=self.db)
        self.assertIsNotNone(board_list, msg="test_02_get_all_board Error")

    def test_03_get_board(self):
        board = self.board_list[-1]
        get_board = service_board.get(db=self.db, id=self.board_list[-1].id)
        self.assertEqual(get_board.id, board.id, msg="test_03_get_board Error")

    def test_04_update_board(self):
        board = self.board_list[-1]
        updating_board = UpdateBoard(
            id=board.id,
            board_status="update_status",
            board_content="update_content",
            parent_id=self.board_list[-3].id,
        )
        updated_board = service_board.update(db=self.db, obj_in=updating_board, db_obj=board)

        self.assertEqual(updating_board.id, updated_board.id, msg="test_04_update_board id Error")

        self.assertEqual(updating_board.board_content, updated_board.board_content,
                         msg="test_04_update_board board_content Error")
        self.assertEqual(updating_board.board_status, updated_board.board_status,
                         msg="test_04_update_board board_status Error")
        self.assertEqual(updating_board.parent_id, updated_board.parent_id, msg="test_04_update_board parent_id Error")

    def test_05_add_catagory_to_board(self):
        board = self.board_list[0]
        add_category = board.team.category_list[-1]
        updating_board = UpdateBoard(
            id=board.id,
            category_list=[
                CategoryWithValue(
                    id=add_category.id,
                    value='create_category',
                ),
            ]
        )
        
        updated_board = service_board.update(db=self.db, obj_in=updating_board, db_obj=board)
        category_id_list = []
        for category in updated_board.category_list:
            category_id_list.append(category.category_id)

        self.assertIn(add_category.id, category_id_list, msg="test_05_add_catagory_to_board id Error")

    def test_06_update_catagory_to_board(self):
        pass

    def test_07_delete_catagory_to_board(self):
        pass

    def test_08_remove_board(self):
        board = self.board_list[-1]
        service_board.remove(db=self.db, id=board.id)
        deleted_board = service_board.get(db=self.db, id=board.id)
        self.assertIsNone(deleted_board, msg="test_08_remove_board Error")
