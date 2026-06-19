from database import students

def viewstudent():
    
    for x in students:
        print(x["name"])
        print(x["age"])
        print(x["course"])


