# shopping_cart.py

#from pprint import pprint

import datetime
from os import path

today = datetime.datetime.now()
total_price = 0 
selected_ids = [] 

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# pprint(products)

#INFO CAPTURE / INPUT

while True: 
        selected_id = input("Please input a product identifier:") #> "9" (string)
        if(selected_id.isdigit()):
            x = int(selected_id)
            if(x > 0 and x <= 20):
                selected_ids.append(selected_id)
            else:
                print("not a valid id")
        else:
            selected_id = selected_id.upper()       
            if selected_id == "DONE":
                break
            else:
                print("not a valid input please type done to end")
            


# INFO DISPLAY/ OUTPUT
response = input("would you like a receipt")
response = response.lower()
if(response != "yes"):
    print("-------------------------------------------------------")
    print("Welcome to Whole Foods")
    print("www.wholefoods.com")
    print("-------------------------------------------------------")
    print("Date: " + str(today.strftime("%x")))
    print("Time: " + str(today.strftime("%I:%M %p")))
    print("-------------------------------------------------------")

    # print(selected_ids)
    print('{:<65} {:<2}'.format("Item(s)", "Price"))
    for selected_id in selected_ids:
            matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
            matching_product = matching_products[0]
            total_price = total_price + matching_product["price"]
            print('{:<65} ${:<0}'.format(matching_product["name"],str(matching_product["price"])))

    print('{:>65} ${:<0}'.format("Total",str(round(total_price))))
    tax = total_price * .08875
    print('{:>65} ${:<0}'.format("Tax",str(round(tax,2))))
    total_price = total_price + tax
    print('{:>65} ${:<0}'.format("Total",str(round(total_price,2))))
    print("-------------------------------------------------------")
    print("Thank you for shopping at Whole Foods")
    print("SEE YOU AGAIN SOON!")
else:
    day = today.strftime("%x").replace("/","-")
    time = today.strftime("%X").replace(":","-")
    file_name = path.relpath("receipts/" + day + "-" + time + ".txt")
    file = open(file_name,"w")
    file.write("------------------------------------------------------- \n")
    file.write("Welcome to Whole Foods \n")
    file.write("www.wholefoods.com \n")
    file.write("------------------------------------------------------- \n")
    file.write("Date: " + str(today.strftime("%x")) + "\n")
    file.write("Time: " + str(today.strftime("%I:%M %p")) + "\n")
    file.write("------------------------------------------------------- \n")

    # print(selected_ids)
    file.write('{:<65} {:<2} \n'.format("Item(s)", "Price"))
    for selected_id in selected_ids:
            matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
            matching_product = matching_products[0]
            total_price = total_price + matching_product["price"]
            file.write('{:<65} ${:<0} \n'.format(matching_product["name"],str(matching_product["price"])))

    file.write('{:>65} ${:<0} \n'.format("Total",str(round(total_price))))
    tax = total_price * .08875
    file.write('{:>65} ${:<0} \n'.format("Tax",str(round(tax,2))))
    total_price = total_price + tax
    file.write('{:>65} ${:<0} \n'.format("Total",str(round(total_price,2))))
    file.write("------------------------------------------------------- \n")
    file.write("Thank you for shopping at Whole Foods \n")
    file.write("SEE YOU AGAIN SOON")

    file.close ()