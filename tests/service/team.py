from tests.base import BaseTest

from sprint.team.service import service_team
from sprint.user.service import service_user

from sprint.team.schema import CreateTeam, UpdateTeam, CreateTeamAddUser, InviteTeam


class Order_02_Service_Team(BaseTest):
    def setUp(self):
        self.user_list = service_user.get_multi(db=self.db)
        self.create_team = CreateTeamAddUser(
            team=CreateTeam(
                team_name='created_team'
            ),
            user_id=self.user_list[-1].id
        )

        self.team_list = service_team.get_multi(db=self.db)

    def test_01_create_team(self):
        created_team = service_team.create_with_user_id(db=self.db, obj_in=self.create_team)
        self.assertEqual(created_team.team_name, self.create_team.team.team_name, msg="test_01_create_team Error")

    def test_02_get_all_team(self):
        team_list = service_team.get_multi(db=self.db)
        self.assertIsNotNone(team_list, msg="test_02_get_all_team Error")

    def test_03_get_team(self):
        team = self.team_list[-1]
        get_team = service_team.get(db=self.db, id=team.id)
        self.assertEqual(get_team.id, team.id, msg="test_03_get_team Error")

    def test_04_update_team(self):
        team = self.team_list[-1]

        updateing_value = UpdateTeam(
            id=team.id,
            team_name="update_teamname",
        )

        updated_team = service_team.update(db=self.db, db_obj=team, obj_in=updateing_value)

        self.assertEqual(updateing_value.id, updated_team.id, msg="test_04_update_team id Error")
        self.assertEqual(updateing_value.team_name, updated_team.team_name, msg="test_04_update_team team_name Error")

    def test_05_invite_user_to_team(self):
        team = self.team_list[-1]
        user = self.user_list[-2]
        invite_schema = InviteTeam(user_id=user.id, id=team.id)
        invited_team = service_team.invite(db=self.db, obj_in=invite_schema)
        self.assertIn(user, invited_team.user_list, msg="test_05_invite_user_to_team Error")

    def test_06_delete_team(self):
        team = self.team_list[-1]
        service_team.remove(db=self.db, id=team.id)
        deleted_team = service_team.get(db=self.db, id=team.id)
        self.assertIsNone(deleted_team, msg="test_06_delete_team Error")
