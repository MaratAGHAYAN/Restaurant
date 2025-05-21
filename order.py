# Ներկայացնում է պատվերը։
# Պարունակում է մենյուի տարրերի ցանկ, ընդհանուր գին և պատվերի ժամանակ։
# Վերադարձնում է ընդհանուր գինը և պատվերների անունները։

class Order:
    def __init__(self, menu_items, order_time, order_price = 0):
        self.__menu_items = menu_items
        self.__order_time = order_time
        self.__order_price = order_price

    def get_menu_items(self):
        return self.__menu_items
    
    def set_menu_items(self, menu_items):
        self.__menu_items = menu_items

    def get_order_price(self):
        price = 0
        for i in self.__menu_items:
            price += i.get_price()
        return int(price)
    
    def set_order_price(self, order_price):
        self.__order_price = order_price

    def get_order_time(self):
        return self.__order_time
    
    def set_order_time(self, order_time):
        self.__order_time = order_time

    def __str__(self):         # generacvox anunnern e tpum
        order_items_names = ""
        for i in self.__menu_items:
            order_items_names += i.get_name() + " "
        return order_items_names
    
    def get_total_price(self):
        return f"{self}, General price = {self.get_order_price()} AMD"
