from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
import models
from database import engine, session_local
from sqlalchemy.orm import Session

# FastAPI = 어플리케이션에서 Jinja2 템플릿 엔진을 사용하도록 설정
templates = Jinja2Templates(directory="template")

app = FastAPI()

# 데이터베이스 테이블 생성
models.Base.metadata.create_all(bind=engine)

# 데이터베이스 세션
def get_db():
    db = session_local() # 호출될때마다 새로운 세션 객체 생성
    try:
        yield db # 데이터 베이스 세션 객체 반환
    finally:
        db.close
        
@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    
    # 데이터베이스에서 Todo 모델을 가져온다.
    todos = db.query(models.Todo).order_by(models.Todo.id.desc())
    
    # 인덱스 템플릿 랜더링
    return templates.TemplateResponse("index.html", {"request" : request, "todos" : todos})