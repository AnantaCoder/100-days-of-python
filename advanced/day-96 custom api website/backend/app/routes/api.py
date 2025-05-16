from fastapi import APIRouter
from app.services.lotr_api import get_movies,get_books

router = APIRouter(prefix="/api")

@router.get("/movies")
async def fetch_movies():
    return await get_movies()

@router.get("/book")
async def fetch_books():
    return await get_books()
