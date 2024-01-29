from abc import ABC, abstractmethod
from base_model import OrderAmount as OrderAmount
from base_enums import OrderItemSize
from custom_exceptions import InvalidOrderItemSize
# created abstract order calculator, which implements OrderCalculator abstract
# Perdorimi i metodes abstrakte (OOP)
class AbstractOrderCalculator(ABC):
    
    def calculate_total_order_amount(self, order):
        order_items = order.get_order_items()
        total_order_amount = 0.0
        for order_item in order_items:
            total_order_amount += self.calculate_order_item_price(order_item)
            
        return total_order_amount
    
    def calculate_order_item_price(self, order_item):
        size_rate_amount = self._get_size_rate_amount(order_item.get_order_item_size())
        product = order_item.get_product()
        total_order_item_price_single = product.get_price() * size_rate_amount
        order_item.set_order_item_price(total_order_item_price_single)
        
        return total_order_item_price_single * order_item.get_quantity()
    
        #if(order.item_quantity() == 0):
        #raise ValueError("Invalid order item quantity")
    
    
# krijimi i një metode të ofruar nga klasa abstrakte për të gjitha nën-klasat
    def get_vat_rate(self, decimal):
        if decimal == True:
            return self._get_vat_rate()
        else:
            return self._get_vat_rate() * 100
 
    def calculate_total_order_amount_vat(self, total_order_amount):
            return total_order_amount * self._get_vat_rate()
        
    # call the method to calculate the total order amount from object of OrderClaculator by providing order as a parameter
    def calculate_order_amount(self, order): 
        total_order_amount = self.calculate_total_order_amount(order)
        
        # llogaritni shumën e TVSH-së dhe shtoni shumën totale të porosisë me TVSH-në si variabël të vet
        total_order_amount_vat = self.calculate_total_order_amount_vat(total_order_amount)
        total_order_amount_with_vat = total_order_amount + total_order_amount_vat
        order_amount = OrderAmount(total_order_amount, total_order_amount_vat, total_order_amount_with_vat)
        return order_amount
    # krijimi i implementimit të metodës abstrakte për të llogaritur TVSH-në e shumës totale të porosisë
    @abstractmethod        
    def _get_vat_rate(self):
        pass
    @abstractmethod        
    def _get_size_rate_amount(self, order_itemsize):
        pass
 
 # krijimi i nje classe te re, e cila zgjeron AbstractOrderCalculator
class OrderCalculatorKS (AbstractOrderCalculator):
    
    # defined constant variable for VAT rate
    def __init__(self):
        self.__VAT_RATE = 0.18
    def _get_vat_rate(self):
        return self.__VAT_RATE
 
    def _get_size_rate_amount(self, order_item_size):
        match order_item_size:
            case OrderItemSize.SMALL:
                return 0.7
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.2
            case OrderItemSize.XXL:
                return 1.25
            case _:
                raise InvalidOrderItemSize("No Valid order item size: " + order_item_size)
                return 1
# krijimi i nje klasë të re, e cila klasë zbaton llogaritësin AbstractOrder
class OrderCalculatorGER (AbstractOrderCalculator):
    # ndryshore e përcaktuar për normën e TVSH-së si konstante përfundimtare
    __VAT_RATE = 0.19
 
    def _get_vat_rate(self):
                return self.__VAT_RATE
    def _get_size_rate_amount(self, order_item_size):
        match order_item_size:
            case OrderItemSize.SMALL:
                return 0.8
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.25
            case OrderItemSize.XXL:
                return 1.3
            case _:
                raise InvalidOrderItemSize("No Valid order item size: " + order_item_size)
                return 1