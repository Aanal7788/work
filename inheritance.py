# inheritance:one class derived properties of another class is called inheritance
# PARENT CHILD relationship
# inheritance provide reusability
# using of inheritance we can reduce our properties(code) and save time

# there are total 5 types of inheritance
# 1)single level
# 2)multi level
# 3)multiple inheritance
# 4)hiearchical
# 5)hybrid inheritance
# _____________________________________________
# single level inheritance
# _________________________________________________________
class parent:
    def display(self):
        print("hello,parent class method called")

class child(parent):
    def child_display(self):
        print("hello,child class method called")

obj=child()
obj.display()
obj.child_display()

# ________________________________________________________________
# multi level inheritance=class A--->class B--->class C
# _________________________________________________________

class A:
    def displayA(self):
        print("A class display")
class B(A):
    def displayB(self):
        print("B class display")
class C(B):
    def displayC(self):
        print("C class display")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()