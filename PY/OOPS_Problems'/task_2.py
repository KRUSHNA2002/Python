class employee:

    def __init__(self,emp_id,name,salary,department):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
        self.department=department

    def show_deatails(self):
        print("Employee Id is : ",self.emp_id)
        print("Employee name is : ",self.name)
        print("Employee salary is : ",self.salary)
        print("Employee department is : ",self.department)

    def increase_salary(self,amount):
        self.salary +=amount

        return self.salary

    def change_department(self,new_department):

         self.department=new_department



         return self.department

         
    
emp1 = employee( 101,"Krushna",50000,"PHP Developer")

emp1.show_deatails()
print("Salary Updated : ",emp1.increase_salary(20000))
print("New Department is : ", emp1.change_department("AI Developer"))

print(emp1.show_deatails())

        

