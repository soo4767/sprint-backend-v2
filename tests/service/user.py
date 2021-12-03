from tests.base import BaseTest

from sprint.user.service import service_user

from sprint.user.schema import CreateUser, UpdateUser


class Order_01_Service_User(BaseTest):
    def setUp(self):
        self.create_user = CreateUser(
            username="test_1",
            password="password_1",
        )
        self.identifier_username = "test_1"

        self.identifier_user_id = 1

        self.login_user = {
            "username": "test_1",
            "password": "password_1",
        }

    def test_01_create_user(self):
        created_user = service_user.create(db=self.db, obj_in=self.create_user)
        self.assertEqual(created_user.username, self.create_user.username, msg="test_01_create_user Error")

    def test_02_get_all_user(self):
        user_list = service_user.get_multi(db=self.db)
        self.assertIsNotNone(user_list)

    def test_03_get_user(self):
        user = service_user.get(db=self.db, id=self.identifier_user_id)
        self.assertEqual(self.identifier_user_id, user.id)

    # TODO 여기서부터 시작함
