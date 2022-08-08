from abc import ABC,abstractmethod
#ABC : Abstract Base Class
class RBI(ABC):
    @abstractmethod
    def roi(self):
        pass

class SBI(RBI):
    def display(self):
        print("SBI")

    def roi(self):
        print("8.7")

s = SBI()
s.display()
s.roi()