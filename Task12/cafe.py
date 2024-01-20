# TASK Requirements:
#    Imagine you are running a cafe.
# 1. Create a list called menu, which should contain at least four items sold in the cafe.
# 2. Create a dictionary called stock, which should contain the stock value for each item on your menu.
# 3. Create another dictionary called price, which should contain the prices for each item on your menu.
# 4. Calculate the total_stock worth in the cafe. You will need to remember to loop through the appropriate dictionaries and lists to do this.
# 5. Print out the result of your calculation.

# Tip: When you loop through the menu list, the ‘items’ can be set as keys to access the corresponding ‘stock’ and ‘price’ values. 
# Each ‘item_value’ is calculated by multiplying the stock value by the price value.

#1
menu = ["americano", "cappuccino", "latte", "espresso", "blueberry muffin", "almond croissant", "chocolate chip cookie", "pain au raisin"]

#2
stock = {
    "americano": 80,
    "cappuccino": 50,
    "latte": 50,
    "espresso": 100,
    "blueberry muffin": 10,
    "almond croissant": 15,
    "chocolate chip cookie": 24,
    "pain au raisin": 15 
}

#3
price = {
    "americano": 3.19,
    "cappuccino": 3.79,
    "latte": 3.79,
    "espresso": 2.89,
    "blueberry muffin": 3.69,
    "almond croissant": 3.19,
    "chocolate chip cookie": 2.89,
    "pain au raisin": 2.99 
}

print("\nWelcome to your first Python Cafe franchise! Here is our standard menu:\n")

#4
for item in menu:
    print(f"\t{item} ..... £{price[item]}")

total_stock = 0

for item in menu:
    item_value = stock[item] * price[item]  # total item value is calculated by multiplying the stock value(quanitity) by its price
    total_stock = total_stock + item_value  # adding the total value of all items in the cafe


#5
print(f"\nYour current stock in the cafe is worth: £ {total_stock:.2f} \nGood Luck!")

