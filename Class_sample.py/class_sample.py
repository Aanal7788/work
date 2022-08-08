# OOPS:object oriented programing system
# class
# object
# encapsulation
# inheritance
# data abstraction
# polymorphism

# class: class is a collection of data member(variable) and memberfunction(method of function) which is contain data member and member function in a single entity

# object: object is a variable of class

#     using of object we can access properties of class.

# syntax: 
# class classname
#     properties

# obj=classname()

# ___________________________________

# class sample:
#     num1 = 10
#     num2 = 20

# obj = sample()
# print(obj.num1)
# print(obj.num2)
# _________________________________________

# self: which is represent current class properties

# class student:
#     def display(self,fname,lname):
#         print("hello")
#         print("fname = ",fname)
#         print("lname = ",lname)
# obj = student()
# obj.display("Aanal","vora")
# __________________________________________

# class practical:
#     def findfactorial(self,num):
#         f=1
#         for i in range(1,num+1):
#             f*=i

#         print("factorial =",f)

# obj=practical()
# num=int(input('enter a number : '))
# obj.findfactorial(num)

# *******************************************

# # difference between method and function
# # 1) function : which is declare outside the class
#             function are independent

#             def myfun():
#                 statement
# # 2) method : which is declare inside the class
#         method are dependent on class-object

#         def myfun():
#             statement
# ***********************************************

# encapsulation : data, member and member function contain in single entity is called encapsulation
# e.g class

# ************************************************************

# class student:
#     def setName(self,name):
#         self.name=name

#     def getName(self):
#         return self.name
#     def setSubject(self,subject):
#         self.subject=subject
#     def getSubject(self):
#         return self.subject

# obj = student()
# obj.setName("Aanal")
# obj.setSubject("python")

# print("name = ",obj.getName())
# print("subject = ",obj.getSubject())
# __________________________________________________