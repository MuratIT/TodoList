from fastapi import FastAPI, APIRouter

from Users import user_routers
from TodoList import todo_list_router

from settings import settings

app = FastAPI()
router = APIRouter(prefix=settings.base_url)

router.include_router(
    user_routers,
)

router.include_router(
    todo_list_router,
)

app.include_router(
    router
)
