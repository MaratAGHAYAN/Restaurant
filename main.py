
# Ծրագրի մեկնարկային կետն է։
# Բացում է ռեստորանը։
# Ընդունում է պատվերների քանակ։
# Գեներացնում է պատահական պատվերներ։
# Մշակում է պատվերները։
# Փակում է ռեստորանը։
# Ստեղծում է մենյուի CSV ֆայլ։

from restaurant import Restaurant
import csv
restaurant = Restaurant() 
restaurant.open()
orders_count = int(input("Input orders count: "))
print()
orders = restaurant.generate_orders(orders_count)
restaurant.process_orders(orders)
restaurant.close()


data = [
    ("Burger", ["Bun", "Patty", "Sauce", "Tomato", "Cheese"], 3900.0, 400, 3),
    ("Salad", ["Mix_Lettuce", "Tomato", "Cucumber", "Yellow_Pepper", "Feta_Cheese", "Olives", "Olive_Oil"], 2500.0, 300, 5),
    ("Pizza", ["Dough", "Tomato_Sauce", "Pepperoni", "Ham", "Bacon", "Olives", "Mozzarella"], 3000.0, 600, 1),
    ("Pasta", ["Chicken", "Mushrooms", "Parmesan", "Cream"], 2900.0, 500, 2),
    ("Steak", ["Beef", "Vegetables", "Seasonings"], 1200.0, 360, 4)
]

csv_filename = "menu_data.csv"

with open(csv_filename, mode='w', newline='') as file: # bacvum e file, mejy grvum data-n
    writer = csv.writer(file)
    writer.writerow(["id", "name", "ingredients", "price", "priority"]) # vernagir
    for i, (name, ingredients, price, priority, _) in enumerate(data, start=1): # tvyalnery file-um
        writer.writerow([i, name, ", ".join(ingredients), price, priority])
