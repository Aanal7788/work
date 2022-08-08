all_laptop = {
    "dell" : 65000,
    "hp" : 45000,
    "lenovo" : 25000
}

all_mobile={
    "samsung": 85000,
    "mi": 7850,
    "vivo": 25000
}
customer_cart={}

def viewlaptop():
    print("\n LAPTOP LIST : \n")
    for k ,v in all_laptop.items():
        print(f"{k}={v}")

def viewmobile():
    for k, v in all_mobile.items():
        print(f"{k}: {v}")

def purchaseLaptop(laptop_name,qty):
    if laptop_name in  all_laptop:
        price = all_laptop[laptop_name]
        total_price = qty * price
        print('total price =', total_price)
        return total_price

def addTocart(customername,product,productname,qty,price):
    specification = {}
    if customername not in customer_cart:
        specification["product_name"]= productname
        specification["qty"]=qty
        specification["total_price"]=price

        customer_cart[customername]=specification

        print(customer_cart)
        