from tests.base import BaseTest

from sprint.team.service import service_team
from sprint.category.service import service_category

from sprint.category.schema import CreateCategory, UpdateCategory


class Order_04_Service_Category(BaseTest):
    def setUp(self):
        self.team_list = service_team.get_multi(db=self.db)
        self.create_category = CreateCategory(
            category_name='create category',
            team_id=self.team_list[-1].id
        )

    def test_01_create_category(self):
        created_category = service_category.create(db=self.db, obj_in=self.create_category)
        self.assertEqual(created_category.category_name, self.create_category.category_name,
                         msg="test_01_create_category Error")

    def test_02_update_category(self):
        team = self.team_list[-1]

        updateing_category = UpdateCategory(
            id=team.category_list[-1].id,
            category_name="updated_category_title",
        )

        updated_category = service_category.update(db=self.db, db_obj=team.category_list[-1], obj_in=updateing_category)

        self.assertEqual(updated_category.id, updated_category.id, msg="test_02_update_category id Error")
        self.assertEqual(updated_category.category_name, updated_category.category_name,
                         msg="test_02_update_category category_name Error")

    def test_03_remove_team(self):
        category = self.team_list[-1].category_list[-1]
        service_category.remove(db=self.db, id=category.id)
        deleted_team = service_category.get(db=self.db, id=category.id)
        self.assertIsNone(deleted_team, msg="test_03_remove_team Error")
