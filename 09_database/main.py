from fastapi import FastAPI, Depends
from database import session_local, engine
import models, schemas, teacher_crud
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# 제너레이터 함수
# yield : 함수가 제너레이팅한 객체를 반환하게 하는 키워드
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


# teacher 등록
@app.post("/teachers", response_model=schemas.TeacherResponse)
async def create_teacher(teacher: schemas.TeacherCreate,
                        # 세션 객체를 먼저 생성하기 위해 
                        db: Session = Depends(get_db)):
    
    response = teacher_crud.create_teacher(db, teacher)
    
    return response

# teacher 단일 조회
@app.get("/teacher/{teacher_id}", response_model=schemas.TeacherResponse)
async def find_teacher_by_id(teacher_id:int, db: Session = Depends(get_db)):
    
    db_teacher = teacher_crud.get_teacher_by_id(db, teacher_id)
    
    return db_teacher

# teacher 전체 조회
@app.get("/teachers", response_model=list[schemas.TeacherResponse])
async def find_all_teachers(db: Session = Depends(get_db)):
    
    all_teachers = teacher_crud.get_all_teachers(db)
    
    return all_teachers

# teacher 수정
@app.put("/teachers/{teacher_id}", response_model=schemas.TeacherResponse)
async def update_teacher(
    teacher_id:int,
    teacher: schemas.TeacherUpdate,
    db: Session = Depends(get_db)
):
    
    update_teacher = teacher_crud.update_teacher(db,teacher_id, teacher)
    
    return update_teacher

from fastapi import FastAPI, Depends
from database import session_local, engine
import models, schemas, teacher_crud
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# 제너레이터 함수
# 함수가 제너레이팅한 객체를 반환하게 하는 키워드
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

# teacher 등록
@app.post("/teachers", response_model=schemas.TeacherResponse)
async def create_teacher(
    teacher : schemas.TeacherCreate, 
    # 세션 객체를 먼저 생성하기 위해
    db : Session = Depends(get_db)
    ):
    
    response = teacher_crud.create_teacher(db, teacher)
    
    return response

# teacher 단일 조회
@app.get("/teacher/{teacher_id}", response_model=schemas.TeacherResponse)
async def find_teacher_by_id(teacher_id:int, db: Session = Depends(get_db)):
    
    db_teacher = teacher_crud.get_teacher_by_id(db, teacher_id)
    
    return db_teacher

# teacher 전체 조회
@app.get("/teachers", response_model=list[schemas.TeacherResponse])
async def find_all_teachers(db: Session = Depends(get_db)):
    
    all_teachers = teacher_crud.get_all_teachers(db)
    
    return all_teachers

# teacher 수정
@app.put("/teachers/{teacher_id}", response_model=schemas.TeacherResponse)
async def update_teacher(
    teacher_id:int,
    teacher: schemas.TeacherUpdate,
    db: Session = Depends(get_db)
):
    
    updated_teacher = teacher_crud.update_teacher(db, teacher_id, teacher)
    
    return updated_teacher


# teacher 삭제
@app.delete("/teachers/{teacher_id}", status_code=204)
async def delete_teacher(teacher_id:int, db:Session = Depends(get_db)):
    
    teacher_crud.delete_teacher(db, teacher_id)
    
    return None