
class A:

    def first(self):
        print("Class A")


class B(A):
    def second(self):
        print("Class B")



obj=B()

obj.first()
obj.second()