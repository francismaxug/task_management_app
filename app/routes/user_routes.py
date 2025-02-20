from fastapi import APIRouter

user_router = APIRouter()

@user_router.post("/create")
async def create_user(user:str):
    return {
        "message": "Success",
        "data": "data"
    }