import os 
import dotenv
import httpx

dotenv.load_dotenv()

API_KEY =   os.getenv("LORD_OF_THE_RINGS_APIKEY")
BASE_URL = "https://the-one-api.dev/v2"
HEADERS ={
        "Authorization":f"Bearer {API_KEY}"
    }
async def get_movies():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/movie", headers=HEADERS)
        resp.raise_for_status() #error handling
        
        return resp.json()
    
    
async def get_books():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/book", headers=HEADERS)
        resp.raise_for_status() #error handling
        
        return resp.json()
    
    
async def get_book_chapter(book_id: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/book/{book_id}/chapter",headers=HEADERS)
        resp.raise_for_status() #error handling
        return resp.json()