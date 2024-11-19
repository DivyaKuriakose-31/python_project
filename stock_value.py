'''
Author:Divya Kuriakose
Date=19-11-2024
Program to find the highest stock value 
'''


# Inventory data as tuples (item_name,quantity, unit_price)
inventory = [
    ("Laptop",5 ,60000),
    ("Headphone",15,500),
    ("Mouse",50,150),
    ("Keyboard",20,200),
    ("Monitor",10,3000),
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name, quantity, unit_price=item
    stock_value= quantity * unit_price
    print(f"Item Name:{item_name},the stock value is: {stock_value}")
    if stock_value> highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f"Highest stock value is: {highest_stock_value}")
print(f"Item with highest stock value is :{item_with_highest_stock_value}")