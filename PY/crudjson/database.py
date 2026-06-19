import json


students = []


def load_students():

    global students

    try:
        with open("students.json","r") as file:
            data = json.load(file)

            students.extend(data)

    except FileNotFoundError:
        pass

    except Exception as e:
        print("Error:", e)



def save_students():

    try:
        with open("students.json","w") as file:
            json.dump(students,file,indent=4)

    except Exception as e:
        print("Error:", e)