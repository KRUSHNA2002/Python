
class student:

    def __init__(self,name,marks):

        self.name=name
        self.marks=marks

    def total_marks(self):

         total=0
       
         for all in self.marks:
             
             total= total + all


         return total
        
    def percentage(self):

        per=round((self.total_marks()/300)*100)

        return per

    def passfail(self):

        if self.percentage() >= 50:
           return "Student is pass"
        else:
           return "Student is Failed"

        



std1=student("Krushna",[10,20,230])

print("Total marks is : ",std1.total_marks())
print("Percentage is : ",std1.percentage())
print("Result is : ",std1.passfail())

