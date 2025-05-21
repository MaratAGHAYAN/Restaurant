# Ներկայացնում է խոհարարը։
# Պատրաստում է պատվերը (դանդաղեցումով՝ sleep)։
# Ցուցադրում է պատրաստված ուտեստներն ու գինը։
import time
class Chef():  

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname
    
    def set_surname(self, surname):
        self.__surname = surname

    def prepare_order(self, order):
        time.sleep(2)
        print("Preparing order: ", order)
        time.sleep(1*len(order.get_menu_items()))
        print(f"Order is ready by {self.get_name()} {self.get_surname()}: {' '.join(f'{item.get_name()}({item.get_price()})' for item in order.get_menu_items())}, General price = {order.get_order_price()} ֏(AMD)")
