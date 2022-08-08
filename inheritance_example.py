print("select your role")

print(
    """press 1 for doctor
    press 2 for patient"""
    )
role=int(input("enter your role: "))


class User:
    def __init__(self):
        print("User class")

    def input(self):
        self.email = input("enter email : ")
        self.password = input("enter password : ")
status=True
while status:
    if role==1:
        class Doctor(User):
            def doc_input(self):
                self.specification = input("enter specification : ")
            def display(self):
                print("dector email =",self.email)
                print("doctor password = ",self.password)
                print("doctor specification =",self.specification)

        doctor=Doctor()
        doctor.input()
        doctor.doc_input()
        doctor.display()
        break
    else:
        class Patient(User):
            def pat_input(self):
                self.bloodgroup = input("enter bloodgroup : ")
            def display(self):
                print("patient email =",self.email)
                print("patient password = ",self.password)
                print("patient bloodgroup =",self.bloodgroup)

        patient=Patient()
        patient.input()
        patient.pat_input()
        patient.display()
        break

