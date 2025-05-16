from fastapi import APIRouter , HTTPException
from app.services.lotr_api import get_movies,get_books,get_book_chapter

router = APIRouter(prefix="/api")

@router.get("/movies")
async def fetch_movies():
    return await get_movies()

@router.get("/book")
async def fetch_books():
    return await get_books()

@router.get("/book/{book_id}/chapter")
async def fetch_chapters(book_id: str):
    try:
        return await get_book_chapter(book_id)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching chapters: {str(e)}"
        )
