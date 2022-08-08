class studentclass:
    name = "aanal"
    email = ""
    number = ""
    subject = ""
    city = ""
    fees = ""
    marks = ""

    dict1={}

    
    def createstudent(self,firstname,email,contact,subject,city,fees,marks):
        innerdict1 = {}
        self.name = firstname
        self.email = email
        self.subject = subject
        self.number = contact
        self.city = city
        self.fees=fees
        self.marks=marks

        
        innerdict1["email"]=self.email
        innerdict1["subject"]=self.subject
        innerdict1["number"]=self.number
        innerdict1["city"]=self.city
        innerdict1["fees"]=self.fees
        innerdict1["marks"]=self.marks

        self.dict1[firstname]=innerdict1

        print(self.dict1)