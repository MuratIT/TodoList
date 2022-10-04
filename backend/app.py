from fastapi import FastAPI

from Users import user_routers

from settings import settings

app = FastAPI()

app.include_router(
    user_routers,
    prefix=settings.base_url
)


@app.get('/')
async def root():
    return {"hello": "world"}
