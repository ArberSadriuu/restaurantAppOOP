from base_model import Order, OrderItem, OrderAmount
from base_enums import OrderItemSize
class OrderPrinter:
    
    def print_order_info(self, restaurant, client, order, order_amount, vat_rate):
        # përdorni metodën e re të krijuar
        self.__print_order_info_header(client)
        order_products = order.get_order_items()
        for order_product in order_products:
            # përdorni metodën e re të krijuar
            self.__print_order_item_info(order_product)
            
        self.__print_order_info_footer(restaurant, order_amount, vat_rate)
        
    # krijo metodë të re __printOrderItemInfo
    def __print_order_item_info(self, order_item):
        product = order_item.get_product()
        total_order_item_price = order_item.get_order_item_price() * order_item.get_quantity()
        print(str(order_item.get_quantity()) + " X | " + str(product.get_product_id()) + " . " + str(product.get_name()) + ", " + str(order_item.get_order_item_price()) + ", " + str(total_order_item_price) + " Euro")
        
    # krijo metodë të re __printOrderItemInfo
    def __print_order_info_header(self, client):
        print("------------------------------------")
        print("Order from " + (client.get_name()) + ": ")
        print("------------------------------------")
        
    # krijo metodë të re __printOrderItemInfo
    def __print_order_info_footer(self, restaurant, order_amount, vat_rate):
        print("------------------------------------")
        print("The total price of the order is: ")
        print("SUB TOTAL: " + str(order_amount.get_total_order_amount()) + " Euro.")
        print("VAT 18%: " + str(order_amount.get_total_order_amount_vat()) + " Euro. ")
        print("TOTAL: " + str(order_amount.get_total_order_amount_with_vat()) + " Euro. ")
        print("--------------------------------------")
        print(restaurant.get_name() +" in " + restaurant.get_address())
        
class OrderManager:
    def __init__(self):
        self.__orders = []
        
    def get_orders(self):
        return self.__orders
    
    def create_order(self, menu):
        order = Order()
        self.add_order_item(order, menu.get_menu_items().get(100), 1, OrderItemSize.XXL)
        self.add_order_item(order, menu.get_menu_items().get(101), 1, OrderItemSize.MEDIUM)
        self.add_order_item(order, menu.get_menu_items().get(200), 2, OrderItemSize.LARGE)
        self.add_order_item(order, menu.get_menu_items().get(201), 3, OrderItemSize.SMALL)
        
        return order

    def add_order_item(self, order, product, quantity, order_item_size):
        order_item = self.create_order_item(product, order_item_size, quantity)
        order.get_order_items().append(order_item)
        
    def create_order_item(self, product, order_item_size, quantity):
        order_item = OrderItem(product, order_item_size, quantity)
        return order_item
        
# Klasa per klasifikimin e te dhenave ne fatur
class InvoiceBuilder:
    # Ketu do te merren te dhenat prej porosise
    def get_order_info(self, restaurant, client, order, order_amount, vat_rate):
        order_info = self.__get_order_info_header(client) # tek kjo pjesa e header do te paraqiten informatat e klientit ne fature
        
        order_items = order.get_order_items()
        for order_item in order_items:
            order_info += self.__get_order_item_info(order_item)  #me kete kemi iteraur 
            #                 neper produkte deri sa i kemi marr produktet te cilat i ka kerkuar klienti dhe i kemi paraqitur ne fatur
            
        order_info += self.__get_order_info_footer(restaurant, order_amount, vat_rate)  # me kete kemi treguar 
                          # qe ne fund te fatures duhet te paraqitet emri i restaurantit, shuma totale dhe TVSH
        return order_info
    
    def __get_order_item_info(self, order_item):
        product = order_item.get_product()   # ketu e kemi barazuar produktin me artikujt e porositur
        total_order_item_price = order_item.get_order_item_price() * order_item.get_quantity() # ketu kemi thene qe varesisht nga 
        #                                                                              sasia do te rritet edhe qmimi i produkteve
        
        
        
        #Informata rreth produktit qe porositet dhe kjo eshte pjesa qe tregon se qfar ka porositur klienti ne fatur
        order_item_info = (
            f"{order_item.get_quantity()} x| {product.get_product_id()}."
            f"{product.get_name()} | {order_item.get_order_item_price()} | {total_order_item_price} Euro\n"
            
        )
        return order_item_info
    
    #Pjesa qe do te paraqitet ne fillim te fatures si prsh nga kush eshte porositur ky produkt apo keto 
    def __get_order_info_header(self, client):
        
        order_header = (
            f"Order from {client.get_name()} : \n"
            "-------------------------------------"
        )
        return order_header
    #Pjesa qe do te paraqitet ne fund te fatures si pjesa e qmimit total, TVSH etj.
    def __get_order_info_footer(self, restaurant, order_amount, vat_rate):
        order_footer = (
            "-------------------------------------\n"
            "The total price of this order is: \n "
            f"SUB TOTAL:{order_amount.get_total_order_amount()} Euro. \n"
            f"VAT {int(vat_rate)}% {order_amount.get_total_order_amount_vat()} Euro. \n"
            f"TOTAL: {order_amount.get_total_order_amount_with_vat()} Euro. \n"
            "--------------------------------------\n"
            f"{restaurant.get_name()} in {restaurant.get_address()} \n"
        )
        return order_footer