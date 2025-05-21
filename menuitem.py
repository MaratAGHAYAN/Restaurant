# Ներկայացնում է մենյուի տարրը։
# Պարունակում է անուն, բաղադրիչներ, գին, առաջնահերթություն և պատրաստման տևողություն։
class MenuItem:
    
    def __init__(self, name, ingredients, price, priority, duration):
        self.__id = id(self)  
        self.__name = name
        self.__ingredients = ingredients
        self.__price = price
        self.__priority = priority
        self.__duration = duration 

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_ingredients(self):
        return self.__ingredients
    
    def set_ingredients(self, ingredients):
        self.__ingredients = ingredients

    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

    def get_priority(self):
        return self.__priority
    
    def set_priority(self, priority):
        self.__priority = priority
        
    def get_duration(self):
        return self.__duration
    
    def set_duration(self, duration):
        self.__duration = duration