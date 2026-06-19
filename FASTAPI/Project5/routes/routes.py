from fastapi import APIRouter
from services import controller
from schemas.users import Student

router=APIRouter(
    prefix="/students",
    tags=["students"]
)
@router.get("/")
def get_students():
    return controller.get_all()

@router.post("/")
def add_students(student:Student):
    return controller.create(student)

@router.put("/{student_id}")
def update_student(student_id:int,data:Student):
    return controller.update(student_id,data)


@router.delete("/{student_id}")
def delete_student(student_id:int):

    return controller.delete(student_id)