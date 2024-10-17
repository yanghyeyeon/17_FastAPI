from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/items/")
async def read_items(request : Request):
    # 클라이언트 ip
    host = request.client.host
    # request
    # body() : 본문
    # headaers : 헤더
    return {"clienthost" : host}

# request Body
# 클래스타입으로 만들고, BaseModel을 상속받아 구현한다.
from pydantic import BaseModel

class Teacher(BaseModel):
    is_working: bool
    name: str
    nickname: str | None = None # Optional
    
@app.post("/teachers")
async def teacher__info(teacher: Teacher):
    if teacher.nickname:
        return f"안녕하세요 제 닉네임은 {teacher.nickname}이고, 현재 일하는 상태는 {teacher.is_working}입니다."
    return f"안녕하세요 제 이름은 {teacher.name}이고, 현재 일하는 상태는 {teacher.is_working} 입니다"


# FastAPI
# path_parameter -> url에 선언을 한다.
# requestBody -> 클래스 타입의 매개변수라면
# query_paramether -> 그외

# 만들어보기

# (int)student_no : path_parameter로 받고
# Student : requestBody (이름(str), 나이(int))
# (str)lecture_name : query_parameter

# student no, name, age, lecture_name 을 전부 출력하는 문자열로 return 해주는 api

class Student(BaseModel):
    name: str
    age: int

@app.post('/students/{student_no}')
async def student_info(
    student: Student,
    lecture_name: str,
    student_no : int
    ):
    return f"student_no는 {student_no}이고, 이름은 {student.name}이고 나이는 {student.age}이고 lecture_name은 {lecture_name} 입니다."