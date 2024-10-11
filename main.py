

from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import create_tables, delete_tables
from routers import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DB cleared")
    await create_tables()
    print("DB is ready")
    yield
    print("OFF")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)







