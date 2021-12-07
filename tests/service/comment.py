from tests.base import BaseTest

from sprint.team.service import service_team
from sprint.comment.service import service_comment
from sprint.comment.schema import CreateComment, UpdateComment


class Order_05_Service_Comment(BaseTest):
    def setUp(self):
        self.team = service_team.get_multi(db=self.db)[-1]
        self.create_comment = CreateComment(
            content='comment_content',
            board_id=self.team.board_list[-1].id,
            user_id=self.team.user_list[-1].id
        )

    def test_01_create_comment(self):
        created_comment = service_comment.create(db=self.db, obj_in=self.create_comment)
        self.assertEqual(created_comment.content, self.create_comment.content, msg="test_01_create_comment Error")

    def test_02_update_comment(self):
        comment = self.team.board_list[-1].comment_list[-1]

        updateing_comment = UpdateComment(
            id=comment.id,
            content=comment.content
        )

        updated_comment = service_comment.update(db=self.db, db_obj=comment, obj_in=updateing_comment)

        self.assertEqual(updateing_comment.id, updated_comment.id, msg="test_02_update_comment id Error")
        self.assertEqual(updateing_comment.content, updated_comment.content, msg="test_02_update_comment content Error")

    def test_03_delete_comment(self):
        comment = self.team.board_list[-1].comment_list[-1]
        service_comment.remove(db=self.db, id=comment.id)
        deleted_comment = service_comment.get(db=self.db, id=comment.id)
        self.assertIsNone(deleted_comment, msg="test_03_delete_comment Error")
