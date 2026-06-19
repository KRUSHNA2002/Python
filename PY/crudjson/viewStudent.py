from database import students

def viewstudent():

    if len(students)==0:
        print("Student Not Found")
        return
    
    for x in students:
        print("<---------------->")
        print("Name -> ", x["name"])
        print("Age -> ", x["age"])
        print("Course -> ", x["course"])


