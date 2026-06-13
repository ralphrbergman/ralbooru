from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from config import templates

index_router = APIRouter()

@index_router.get("/", response_class = HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request = request, name = "index.html")
