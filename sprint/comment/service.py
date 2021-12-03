from sprint.service.service_base import ServiceBase
from schema import CreateComment, UpdateComment
from model import Comment as CommentModel


class Team(ServiceBase[CommentModel, CreateComment, UpdateComment]):
    pass
 