class Student:
    # def___init___(self)
    print("welcome to tops technologies")

    def inputDetails(self,fname,lname,subject,marks):
        self.firstname=fname
        self.lastname=lname
        self.subject=subject
        self.marks=marks

    def displaydetails(self):
        print("firstname=",self.firstname)
        print("lastname=",self.lastname)
        print("subject=",self.subject)
        print("marks=",self.marks)

class Faculty:
    # def___init___(self)  
    print("welcome to tops technologies")

    def inputDetails(self,fname,lname,depart):
        self.firstname=fname
        self.lastname=lname
        self.depart=depart

    def displaydetails(self):
        print("firstname =",self.firstname)
        print("lastname=",self.lastname)
        print("depart =",self.depart)

jay=Student()
jay.inputDetails("jay","pathak","python",78)
jay.displaydetails()