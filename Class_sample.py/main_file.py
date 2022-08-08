import faculty,student

f=faculty.facultyclass()
s=student.studentclass()

print(f.name)
print(s.name)

# f.createfaculty("aanal","a@gmail.com","9328583149","python","ahmedabad")

# print(f.name)
# print(f.number)

status = True

while status:
    fname = input("enter faculty name: ")
    email = input("enter faculty email: ")
    mobile = input("enter mobile number: ")
    subject = input("enter  faculty subject: ")
    city = input("enter faculty city: ")
    

    f.createfaculty(fname, email, mobile, subject, city)
    choice = input("do you want to make details press 'y' for yes and press 'n' for no: ")

    if choice == 'y':
        status = True
    else: 
        status = False

status = True

while status:
    fname = input("enter student name: ")
    email = input("enter student email: ")
    mobile = input("enter mobile number: ")
    subject = input("enter student subject: ")
    city = input("enter student city: ")
    fees = input("enter fees:")
    marks=input("enter marks: ")

    f.createstudent(fname,email,mobile,subject,city,fees,marks)
    choice = input("do you want to make details press 'y' for yes and press 'n' for no: ")

    if choice == 'y':
        status = True
    else: 
        status = False

