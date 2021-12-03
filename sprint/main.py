from fastapi import FastAPI

from database import engine
from sprint.board import model as board_model
from sprint.category import model as category_model
from sprint.comment import model as comment_model
from sprint.team import model as team_model
from sprint.user import model as user_model
from sprint.routers import user as user_router
from sprint.routers import team as team_router

app = FastAPI()

models = [
    board_model,
    category_model,
    comment_model,
    user_model,
    team_model,
]

for model in models:
    model.Base.metadata.create_all(engine)

app.include_router(user_router.router)
app.include_router(team_router.router)

import uvicorn
from pathlib import Path
import os
import sys

if __name__ == "__main__":
    path = Path(os.path.realpath(__file__)).parent.parent.absolute()
    sys.path.append(str(path))
    uvicorn.run("spint.main:app", host="0.0.0.0", reload=True, port=8000)
