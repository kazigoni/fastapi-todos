from fastapi import APIRouter

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/")
def all_users():
    return "No Users yet"
