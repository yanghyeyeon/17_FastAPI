from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException

# student를 저장하는 서비스로직
def create_student(db : Session, student = schemas.StudentCreate):
    
    # 저장할 student 객체 만들기
    db_student = models.Student(
        name=student.name,
        nickname=student.nickname,
        lunch_menu=student.lunch_menu,
        description=student.description
    )
    
    db.add(db_student)
    db.commit()
    
    return db_student

# ID로 student 찾기
def get_student_by_id(db : Session, student_id: int):
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    return found_student

# 모든 student 찾기
def get_all_students(db : Session):
    # 모든 Student 모델 가져오기
    all_students = db.query(models.Student).all()
    
    return all_students

# student 수정하기
def update_student(db: Session, student_id:int, student: schemas.StudentUpdate):
    
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if found_student is None:
        raise HTTPException(status_code=404, detail="Student not Found")
    
    
    if student.name is not None:
        found_student.name = student.name
        
    if student.lunch_menu is not None:
        found_student.lunch_menu = student.lunch_menu
        
    if student.nickname is not None:
        found_student.nickname = student.nickname
        
    if student.description is not None:
        found_student.description = student.description
    
    db.commit
    
    return found_student


def delete_student(db: Session, student_id: int):
    
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if found_student is None:
        raise HTTPException(status_code=404, detail="Student not Found")
    
    db.delete(found_student)
    
    db.commit()