from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import index_router

app = FastAPI()
app.mount("/static", StaticFiles(directory = "static"), name = "static")

app.include_router(index_router)
