class MobileStore:
    def __init__(self):
        self.mobile=4500
        self.__laptop=45000

    def display(self):
        print("mobile = ",self.mobile)
        print("laptop = ",self.__laptop)

    def changeprice(self,newprice):
        self.__laptop=newprice


obj=MobileStore()
obj.display()

obj.mobile=7850
obj.__laptop=50000

obj.display()
print("__change price__")

obj.changeprice(75000)
obj.display()

