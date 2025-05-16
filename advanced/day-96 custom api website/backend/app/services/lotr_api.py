import os 
import dotenv
import httpx

dotenv.load_dotenv()

API_KEY =   os.getenv("LORD_OF_RUINGS_APIKEY")
BASE_URL = "https://the-one-api.dev/v2"

async def get_movies():
    headers ={
        "Authorization":f"Bearer {API_KEY}"
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/movie", headers=headers)
        return resp.json()
    
    
async def get_books():
    headers ={
        "Authorization":f"Bearer {API_KEY}"
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/book", headers=headers)
        return resp.json()