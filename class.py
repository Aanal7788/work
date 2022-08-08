class vehicle:
    def__init__(self.vehicle_type)
    print("VEHICLE CLASS")
    self.vehicle_type=vehicle_type

    def inputDetails(self):
        if self.vehicle_type=="car":
           self.brand = input("enter brand :")
           self.wheels=int(input("enter wheels:"))

        elif self.vehicle_type=="bike":
            self.brand= input("enter brand:")
            self.wheels=int(input("enter wheels:"))

        else:
            print("sorry information not available")

    def display(self):
        print("brand:",self.brand)
        print("wheels:",self.wheels)

car=Vehicle("car")
car.inputDetails()
car.display()

bike=vehicle("bike")
bike.inputDetails()
bike.display()