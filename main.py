from fastapi import FastAPI

from api.get_wishes import get_wishes_from_db

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "alive"}

@app.get("/getWishes")
async def get_wishes(amount: int = 0):
    wishes = await get_wishes_from_db(amount=amount)
    return wishes


