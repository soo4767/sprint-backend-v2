from sprint.service.service_base import ServiceBase
from .schema import CreateUser, UpdateUser
from .model import User as UserModel


class ServiceUser(ServiceBase[UserModel, CreateUser, UpdateUser]):
    pass


service_user = ServiceUser(UserModel)
