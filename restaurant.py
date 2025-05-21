# Ռեստորանի հիմնական կառավարիչ դասն է։
# Բացում/փակում է ռեստորանը։
# Բեռնում է խոհարարներ, մատուցողներ և մենյու ֆայլերից։
# Գեներացնում և մշակում է պատվերներ։
from server import Server
from chef import Chef
from order import Order
from menuitem import MenuItem
import random
import csv
import json

class Restaurant:
    def __init__(self, menu_file="menu_data.csv", worker_file="worker_names.txt"):
        self.__server = self.load_server_from_file(worker_file)["servers"] # worker_file -i servers-ic stanum e anuny matucoxu veragrum serverin
        self.__chef = self.load_chef_from_file(worker_file)["chefs"]
        self.__is_opened = False
        self.__allowed_menu_items = self.load_menu_from_file(menu_file) # stanum e cucaky menu_file-ic

    def load_menu_from_file(self, filename): # stanum e file-ic tvyalnery
        menu_items = [] 
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # vernagir
            for row in reader:
                name = row['name']
                ingredients = [ingredient.strip() for ingredient in row['ingredients'].split(",")] # ingredient listy verartadrum a
                price = float(row['price'])
                priority = int(row['priority'])
                duration = int(row.get('duration', 0))  # avelacnum enq duration ete ete chlini durationy 0 e grvum
                menu_item = MenuItem(name, ingredients, price, priority, duration)
                menu_items.append(menu_item)
        return menu_items
   
    
    def load_server_from_file(self, filename):     #  json
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def load_chef_from_file(self, filename): #  Json
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def open(self):
        self.__is_opened = True
        print("Restaurant opened.")

    def close(self):
        if not self.__is_opened:
            print("\nRestaurant already closed.")
        else:
            self.__is_opened = False
            print("\nRestaurant closed.")

    def generate_orders(self, orders_count):       # generacnum e [1-5] patver, hashvum e dranc yndhanur gumary
        generated_orders = []
        for i in range(orders_count):
            count_of_menu_items = random.randint(1, 5)
            menu_item_list = []
            order_price = 0
            for j in range(count_of_menu_items):
                menu_item = random.choice(self.__allowed_menu_items)
                menu_item_list.append(menu_item)
                order_price += menu_item.get_price()
            order = Order(menu_items=menu_item_list, order_time=120, order_price=order_price)
            generated_orders.append(order)
        return generated_orders
    
    def process_orders(self, orders):   # chef u server-i anun azgannern e generacnum, talis e funkcianin vor tpvi anunnery
        for order in orders:
            server_dict = random.choice(self.__server)
            server_name = server_dict["name"]
            server_surname = server_dict["surname"]
            server = Server(server_name, server_surname) 
            returned_order = server.take_an_order(order)
            
            chef_dict = random.choice(self.__chef) 
            chef_name = chef_dict["name"]
            chef_surname = chef_dict["surname"]
            chef = Chef(chef_name, chef_surname)  
            chef.prepare_order(returned_order)
























































































    # def compare_agility_and_priority(self):
    #     chef_agility = {chef["name"]: chef["agility"] for chef in self.__chef}
    #     menu_item_priority = {item.get_name(): item.get_priority() for item in self.__allowed_menu_items}
    #     for chef_name, chef_agility_value in chef_agility.items():
    #         for menu_item_name, item_priority in menu_item_priority.items():
    #             if chef_agility_value == item_priority:
    #                 print(f"Chef {chef_name} with agility {chef_agility_value} can prepare menu item {menu_item_name} with priority {item_priority}")


    # def process_orders(self, orders):
    #     for order in orders:
    #         server_dict = random.choice(self.__server)
    #         chef_dict = random.choice(self.__chef)

    #         server_name = server_dict["name"]
    #         server_surname = server_dict["surname"]
    #         server = Server(server_name, server_surname)

    #         chef_name = chef_dict["name"]
    #         chef_surname = chef_dict["surname"]
    #         chef_agility = chef_dict["agility"]
    #         chef = Chef(chef_name, chef_surname)

    #        Փ արդյոք խոհարարի շարժունությունը համընկնում է մենյուի տարրերի առաջնահերթությանը
    #         for menu_item in order.get_menu_items():
    #             menu_item_name = menu_item.get_name()
    #             menu_item_priority = menu_item.get_priority()

    #             if chef_agility == menu_item_priority:
    #                 print(f"Chef {chef_name} with agility {chef_agility} can prepare menu item {menu_item_name} with priority {menu_item_priority}")

    #         returned_order = server.take_an_order(order)
    #         chef.prepare_order(returned_order)