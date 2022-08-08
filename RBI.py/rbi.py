class RBI:
    def __init__(self):
        
        self.__roi = 5
        
    def display(self):
        print(self.__roi)
    

    def updateRoi(self,newroi):
        self.__roi = newroi
