from sprint.service.service_base import ServiceBase
from schema import CreateCategory, UpdateCategory
from model import Category as CategoryModel


class Team(ServiceBase[CategoryModel, CreateCategory, UpdateCategory]):
    pass
 