class facultyclass:
    name = "anjali"
    email = ""
    number = ""
    subject = ""
    city = ""

    dict={}


    def createfaculty(self,firstname,email,contact,subject,city):
        innerdict = {}
        self.name = firstname
        self.email = email
        self.subject = subject
        self.number = contact
        self.city = city

        
        innerdict["email"]=self.email
        innerdict["subject"]=self.subject
        innerdict["contact"]=self.number
        innerdict["city"]=self.city

        self.dict[firstname]=innerdict

        print(self.dict)



    