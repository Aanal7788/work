class Productclass:
    """
    __init__ work as a constructor
    it automatically call when object of class create
    """

    def __init__(self):
        print("welcome to product manager")
        self.mobile = 5000
        self.__laptop = 45000
    def display(self):
        print(self.mobile)
        print(self.__laptop)

    def updatePrice(self,newLaptopPrice):
        self.__laptop = newLaptopPrice
