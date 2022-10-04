from fastapi import APIRouter


from .schemas import UserCreate, UserRead, UserUpdate
from .users import auth_backend, fastapi_users

router = APIRouter()
router_auth = APIRouter(prefix='/auth', tags=['auth'])
router_user = APIRouter(prefix='/users', tags=['users'])


router_auth.include_router(
    fastapi_users.get_auth_router(auth_backend)
)
router_auth.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
router_auth.include_router(
    fastapi_users.get_reset_password_router(),
)
router_auth.include_router(
    fastapi_users.get_verify_router(UserRead),
)
router_user.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)

router.include_router(
    router_auth
)
router.include_router(
    router_user
)
