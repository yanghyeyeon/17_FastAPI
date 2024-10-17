from fastapi import APIRouter

teacher = APIRouter(
    prefix="/api/teacher",
    tags=["teachers"]
)

@teacher.get("/")
async def get_teacher():
    return {"message" : "선생입니다!"}