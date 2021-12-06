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

        self.login_user = {
            "username": "test_1",
            "password": "password_1",
        }

        self.user_list = service_user.get_multi(db=self.db)

    def test_01_create_user(self):
        created_user = service_user.create(db=self.db, obj_in=self.create_user)
        self.assertEqual(created_user.username, self.create_user.username, msg="test_01_create_user Error")

    def test_02_get_all_user(self):
        user_list = service_user.get_multi(db=self.db)
        self.assertIsNotNone(user_list, msg="test_02_get_all_user Error")

    def test_03_get_user(self):
        user = self.user_list[-1]
        get_user = service_user.get(db=self.db, id=user.id)
        self.assertEqual(get_user.id, user.id, msg="test_03_get_user Error")

    def test_04_update_user(self):
        user = self.user_list[-1]

        updateing_value = UpdateUser(
            id=user.id,
            username="update_username",
            password='update_password'
        )

        updated_user = service_user.update(db=self.db, db_obj=user, obj_in=updateing_value)

        self.assertEqual(updateing_value.id, updated_user.id, msg="test_04_update_user id Error")
        self.assertEqual(updateing_value.username, updated_user.username, msg="test_04_update_user username Error")
        self.assertEqual(updateing_value.password, updated_user.password, msg="test_04_update_user password Error")

    def test_05_delete_user(self):
        user = self.user_list[-1]
        service_user.remove(db=self.db, id=user.id)
        deleted_user = service_user.get(db=self.db, id=user.id)
        self.assertIsNone(deleted_user, msg="test_05_delete_user Error")
