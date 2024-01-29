#class restaurant
class Restaurant:
   # Enkapsulimi perdorimi i atributeve private, publike dhe protected
    def __init__(self, name , address) -> None:  
        
        self.__name = name 
        self.__address = address

    def set_name(self, name):
        self.__name = name    
    def get_name(self):      
        return self .__name
    
    def set_address(self, address):
        self.__address = address
    def get_address(self):
        return self .__address

#class client
class Client :
    
    def __init__(self, name , phone_nr) -> None:
        
    #attributes
        self.__name = name
        self.__phone_nr = phone_nr

    def set_name(self, name): 
        self.__name = name    
    def get_name(self):       
        return self .__name
    
    def set_phone_nr(self, phone_nr): 
        self.__phone_nr = phone_nr    
    def get_phone_nr(self):       
        return self .__phone_nr

    
#class product
# Superclass (Trashegimia)
class Product :                                    
    
    def __init__(self, product_id, name, price) -> None: 
       
        #attributes
        self.__product_id = product_id
        self.__name = name 
        self.__price = price

    def set_product_id(self, product_id): 
        self.__product_id = product_id
    def get_product_id(self):       
        return self.__product_id
    
    def set_name(self, name): 
        self.__name = name    
    def get_name(self):       
        return self.__name
    
    def set_price(self, price): 
        self.__price = price    
    def get_price(self):       
        return self.__price
    
# Subclass (Trashegimia)
class Meal(Product):
    def __init__(self, product_id, name, price, description) -> None:
        super().__init__(product_id, name, price)
        
        self.__description = description
        
    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description
        
# Subclass (Trashegimia)
class Drink(Product):
    def __init__(self, product_id, name, price, sugar_free) -> None:
        super().__init__(product_id, name, price)
        
        self.__sugar_free = sugar_free
        
    def is_sugar_free(self):
        return self.__sugar_free
    
    def set_sugar_free(self, sugar_free):
        self.__sugar_free = sugar_free
        
            
#class order
class Order :
    
    def __init__(self):
        #list creation                
        self.__product_list = []      
        
    def get_order_items(self):
        return self.__product_list
    
    
class OrderAmount:
    def __init__(self, total_order_amount, total_order_amount_vat, total_order_amount_with_vat):
       self.__total_order_amount = total_order_amount
       self.__total_order_amount_vat = total_order_amount_vat
       self.__total_order_amount_with_vat = total_order_amount_with_vat
       
    def get_total_order_amount(self):
        return self.__total_order_amount
    
    def set_total_order_amount(self, total_order_amount):
        self.__total_order_amount = total_order_amount
        
    def get_total_order_amount_vat(self):
        return self.__total_order_amount_vat
    
    def set_total_order_amount_vat(self, total_order_amount_vat):
        self.__total_order_amount_vat = total_order_amount_vat
          
    def get_total_order_amount_with_vat(self):
        return self.__total_order_amount_with_vat
    
    def set_total_order_amount_with_vat(self, total_order_amount_with_vat):
        self.__total_order_amount_with_vat = total_order_amount_with_vat
        
    
 #created new class OrderItem për të shkëputur marrëdhënien e drejtpërdrejtë midis porosisë dhe produktit
class OrderItem:
    # konstruktor i artikullit të porosisë
    def __init__(self, product, order_item_size, quantity):
        
        self.__product = product
        self.__order_item_size = order_item_size
        self.__quantity = quantity
        # paraqiti atributin orderItemPrice për të përcaktuar artikullin total të porosisë duke përfshirë
        # product price, quantity and order item size
        self.__order_item_price = float(0.0)
        
    def get_product(self):
        return self.__product
    def set_product(self, product):
        self.__product = product 
        
    def get_order_item_size(self):
        return self.__order_item_size
    def set_order_item_size(self, order_item_size):
        self.__order_item_size = order_item_size 
        
    def get_quantity(self):
        return self.__quantity
    def set_quantity(self, quantity):
        self.__quantity = quantity 
        
    def get_order_item_price(self):
        return self.__order_item_price
    def set_order_item_price(self, order_item_price):
        self.__order_item_price = order_item_price
        
class Menu:
    # Prezantimi i dictionary
    def __init__(self, from_file) -> None:
        self.__menu_items = dict({})       
        self.__initalize_menu_products(from_file)    
        
    
# Krijimi i meotdave për të inicializuar menunë duke shtuar produkte
    def __initalize_menu_products(self, from_file):
        if from_file:
            print("Menu items will be created by importing menu file")
        else:
            self.__menu_items.update({100: Meal("Hamburger", 100, 4.5, "Angus beef patty, tomato, red onion")})
            self.__menu_items.update({101: Meal("Cheeseburger", 101, 5, "Angus beef patty, cheese, tomato, red onion")})
            self.__menu_items.update({102: Meal("Sandwich", 102, 3.5, "Chicken, mayonnaise, peppers")})
            self.__menu_items.update({103: Meal("Hotdog", 103, 3, "Beef, mustard, ketchup, onion, cucumber")})
            self.__menu_items.update({104: Meal("Pizza", 104, 6, "Margarita, tomato sauce, mozarella")})
            self.__menu_items.update({105: Meal("Fries", 105, 2, "french fries with ketchup and mayonnaise")})
            self.__menu_items.update({200: Drink("Coca Cola", 200, 1, False)})
            self.__menu_items.update({201: Drink("Coca Cola Zero", 201, 1, True)})
            self.__menu_items.update({202: Drink("Fanta", 202, 1, False)})
            self.__menu_items.update({203: Drink("Sprite", 203, 1, False)})
            self.__menu_items.update({204: Drink("Red Bull", 204, 2, False)})
            self.__menu_items.update({205: Drink("Coffee", 205, 0.5, False)})
            self.__menu_items.update({300: Meal("Ice cream", 300, 1, "Homemade ice cream")})
            self.__menu_items.update({301: Meal("Waffle", 300, 2.5, "Homemade waffles")})
            self.__menu_items.update({302: Meal("Brownie", 300, 1.5, "Homemade brownies")})
        
    def get_menu_items(self):
        return self.__menu_items 
    