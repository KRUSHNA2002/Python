from database import students

def get_all():
    return students


def create(student):

    students.append(student.model_dump())

    return {"msg":"Student Added"}

def update(student_id,data):

    for student in students:

        if student_id == student["id"]:

            student.update(data.model_dump())

            return {
                "message":"Student Updated Succesfully",
                "data":data
            }
    return {
        "message":"Student Not found",
        
        
    }

def delete(student_id):

    for student in students:

        if student_id==student["id"]:

            students.remove(student)

            return {
                "message":"Student Deleted Succesfully",
                "data":student
            }
        
    return {
        "message":"Student Not found",
      }