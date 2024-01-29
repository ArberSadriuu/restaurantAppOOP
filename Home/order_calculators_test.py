import unittest
import order_calculators
from base_model import Menu, OrderItem, Order
from base_enums import OrderItemSize

#per te ndodhur testimi i ketij file qe kemi koduar ne duhet te shkruajm ne terminal: python -m unittest .\testing\order_calculators_test.py
#created special Abstract Calculator Mock class
# Mock class eshte nje class qe inicializon testimin
class OrderCalculatorMock(order_calculators.AbstractOrderCalculator):
    # Implemeted mock method
    def _get_vat_rate(self):
        return 0.12  #supozimi per testimin e Tvsh
    
    # Implemented mock method 2
    def _get_size_rate_amount(self, orderItemSize):
        return 1.0   #Supozimi per testimin e madhesis se produktit

class AbstractOrderCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.order_calculator_mock = OrderCalculatorMock()
        self.menu = Menu()
        
        #Step 1 = Create test method to test order item price calculations
    def test_calculate_total_order_item_price(self):
        
        # Step 2 = Prepare test objects
        hamburger = self.menu.get_menu_items().get(100)
        order_item = OrderItem(hamburger, OrderItemSize.MEDIUM, 2)
        
        total_order_item_price = self.order_calculator_mock.calculate_order_item_price(order_item)
        
        # Step 3 = Validate results
        self.assertEqual(9.0, total_order_item_price)
        self.assertEqual(4.5, order_item.get_order_item_price())
        
        
        #Step 1 = Create test method to test order item price calculations
        # created test method to test total order price calculation 
        
    def test_calculate_total_order_amount(self):
        
        #Step 2 = Prepare objects
        hamburger = self.menu.get_menu_items().get(100)
        sandwich = self.menu.get_menu_items().get(100)
        coca_cola = self.menu.get_menu_items().get(100)
        ice_cream = self.menu.get_menu_items().get(100)
        
        hamburger_order_item = OrderItem(hamburger, OrderItemSize.MEDIUM, 1)
        sandwich_order_item = OrderItem(sandwich, OrderItemSize.MEDIUM, 1)
        coca_cola_order_item = OrderItem(coca_cola, OrderItemSize.MEDIUM, 2)
        ice_cream_order_item = OrderItem(ice_cream, OrderItemSize.MEDIUM, 2)
        
        order = Order()
        order.get_order_items().append(hamburger_order_item)
        order.get_order_items().append(sandwich_order_item)
        order.get_order_items().append(coca_cola_order_item)
        order.get_order_items().append(ice_cream_order_item)
        
        total_order_amount = self.order_calculator_mock.calculate_total_order_amount(order)
        
        # Step 3 = Evaluate
        self.assertEqual(12.0, total_order_amount)
        
    def test_calculate_total_order_amount_vat(self):
        total_order_amount_vat = self.order_calculator_mock.calculate_total_order_amount_vat(12.0)
        self.assertEqual(1.44, total_order_amount_vat)
        
class OrderCalculatorKSTest(unittest.TestCase):
    def setup(self):
        self.order_calculator_ks = order_calculators.OrderCalculatorKS()
        
    def test_get_vat_rate(self):
        vat_rate = self.order_calculator_ks._get_vat_rate()
        
        self.assertEqual(0.18, vat_rate)
        
    def test_get_size_rate_amounts(self):
        
        size_rate_amount_small = self.order_calculator_ks._get_size_rate_amount(OrderItemSize.SMALL)
        size_rate_amount_medium = self.order_calculator_ks._get_size_rate_amount(OrderItemSize.MEDIUM)
        size_rate_amount_large = self.order_calculator_ks._get_size_rate_amount(OrderItemSize.LARGE)
        size_rate_amount_xxl = self.order_calculator_ks._get_size_rate_amount(OrderItemSize.XXL)
        
        self.assertEqual(0.7, size_rate_amount_small)
        self.assertEqual(1, size_rate_amount_medium)
        self.assertEqual(1.2 , size_rate_amount_large)
        self.assertEqual(1.25, size_rate_amount_xxl)
        
class OrderCalculatorGERTest(unittest.TestCase):
    def setup(self):
        self.order_calculator_ger = order_calculators.OrderCalculatorGER()
        
    def test_get_vat_rate(self):
        vat_rate = self.order_calculator_ger._get_vat_rate()
        
        self.assertEqual(0.19, vat_rate)
        
    def test_get_size_rate_amounts(self):
        
        size_rate_amount_small = self.order_calculator_ger._get_size_rate_amount(OrderItemSize.SMALL)
        size_rate_amount_medium = self.order_calculator_ger._get_size_rate_amount(OrderItemSize.MEDIUM)
        size_rate_amount_large = self.order_calculator_ger._get_size_rate_amount(OrderItemSize.LARGE)
        size_rate_amount_xxl = self.order_calculator_ger._get_size_rate_amount(OrderItemSize.XXL)
        
        self.assertEqual(0.8, size_rate_amount_small)
        self.assertEqual(1, size_rate_amount_medium)
        self.assertEqual(1.25 , size_rate_amount_large)
        self.assertEqual(1.3, size_rate_amount_xxl)
    
             
if __name__ == '__main__':
    unittest.main()