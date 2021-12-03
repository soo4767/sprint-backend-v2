from sprint.service.service_base import ServiceBase
from schema import CreateBoard, UpdateBoard
from model import Board as BoardModel


class Team(ServiceBase[BoardModel, CreateBoard, UpdateBoard]):
    pass
 