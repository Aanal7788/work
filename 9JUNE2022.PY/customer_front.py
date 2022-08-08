from views import *

name = input("enter your name :")

menu = """
            MENU 

            1) LAPTOP
            2)MOBILE

        """

print(menu)

choice = int(input("enter your choice: "))
if choice==1:
    viewlaptop()
    laptop_name = input("enter laptop name you want to purchase: ")
    qty = int(input("enter number of laptop you want to buy: "))
    total_price= purchaseLaptop(laptop_name,qty)
    choice = input("do u want to buy it? press 'y' for yes: ")
    if choice=='y' or choice == 'yes':
        addTocart(name,"laptop",laptop_name,qty,total_price)
elif choice==2:
    viewmobile()
else:
    print("invalid input")
