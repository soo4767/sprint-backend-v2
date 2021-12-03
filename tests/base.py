import unittest
import database
from database import engine

from sprint.user.model import User

from fastapi.testclient import TestClient
from sprint.main import app
from datetime import datetime
from sprint.board import model as board_model
from sprint.category import model as category_model
from sprint.comment import model as comment_model
from sprint.team import model as team_model
from sprint.user import model as user_model

models = [
    board_model,
    category_model,
    comment_model,
    user_model,
    team_model,
]


# Test에서 사용할 공통 함수 및 인자를 여기서 정의해줌
class BaseTest(unittest.TestCase):
    host = 'http://localhost:8080'
    db = database.SessionLocal()

    test_client = TestClient(app)  # Test Requests 를 담당하는 client

    @staticmethod
    def get_user_list():
        for model in models:
            model.Base.metadata.create_all(engine)
        user_list = BaseTest.db.query(User).all()
        return user_list

    @staticmethod
    def date_to_datetime(input_date):
        return datetime(input_date.year, input_date.month, input_date.day)
