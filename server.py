# Ներկայացնում է մատուցողը։
# Ստանում է պատվեր։
# Ցուցադրում է, որ պատվերը վերցվել է։
class Server:  

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

    def take_an_order(self, order):
        print(f"\nServer {self.__name} {self.__surname} take an order: ", order)
        return order
