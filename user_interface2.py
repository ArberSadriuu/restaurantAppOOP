#importimi i elementeve te kivy
from kivymd.uix.datatables import MDDataTable #importimi i tabeles qe do te paraqes informacionin e tabelave
from kivy.lang import Builder # lidhja e python file dhe kivy file
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.metrics import dp

# importimi i python file
from menu_utils import MenuImporter #importimi i menus
from base_model import Order, Product, Client, Restaurant # importohen per arsyje te metodave tek calculate_amount per faturen qe eshte me poshte
from order_calculators import OrderCalculatorKS, OrderCalculatorGER
from order_utils import OrderManager, InvoiceBuilder
from base_enums import OrderItemSize

class RestaurantApp(MDApp):
    
    __selected_product = None # Produktet fillojn nga 0
    
    def build(self):
        Window.size = (900, 600)
        # Lidhja me kivy file # ketij line i kemi shtuar nje self ne fillim qe ta bejme parameter global dhe te mund te perdoret ne secilen pjese te aplikacionit
        self.screen = Builder.load_file('restaurant_app_gui2.kv') 
         
        # Thirrja e elementeve nga kivy file
        first_box_layout = self.screen.ids.first_box_layout
        second_box_layout = self.screen.ids.second_box_layout 
        self.quantity_input = self.screen.ids.quantity_input  
        self.spinner = self.screen.ids.spinner     
        self.check_box_ks = self.screen.ids.check_box_ks 
        self.check_box_gr = self.screen.ids.check_box_gr  
        self.name_field = self.screen.ids.name_field 
        self.phone_field = self.screen.ids.phone_field  
        self.invoice_label = self.screen.ids.invoice_label   
             
        #importimi i listes se menus
        menu_importer = MenuImporter()
        menu = menu_importer.import_menu('menu-list.csv')
        
        product_list = list(menu.get_menu_items().values())
        table_row_data = []
        
        #trajtimi i id, name, price ne nje rresht te vetem
        for product in product_list:
            table_row_data.append((product.get_product_id(), product.get_name(), product.get_price())) 
           
        
        menu_table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.5),
            check = True,
            rows_num = 10,
            column_data = [         
                ("Id", dp(30)),
                ("Name", dp(75)),              
                ("Price", dp(30))
            ],
            
            row_data = table_row_data             
        )  # tek pjesa e mesiperme deri tek commentet kemi bere copy paste nga user_interface.py pasi qe 
           #eshte e njejta pjese dhe sherben per importimin e menus dhe per tabelen e pare qe eshte mddatatable
        
        # Shtimi i menuse ne first box layout
        first_box_layout.add_widget(menu_table) 
        menu_table.bind(on_row_press=self.on_row_press) 
        
        # sherben per ti paraqitur produktet e porositura
        self.order_table = MDDataTable (
            size_hint=(1,1),
            padding= [0,30,0,0],
            check = True,
            rows_num = 10,
            #te dhenat neper kolona
            column_data = [
                ("Id", dp(20)),
                ("Name", dp(20)),              
                ("Price", dp(20)),
                ("Quantity", dp(20)),
                ("Size", dp(20))                             
            ],
            row_data = []
        )
        second_box_layout.add_widget(self.order_table)

        # Metode per lidhjen e id, name, price, quantity, size me funskionet e veta
        # Nese klikohet diqka ne tabel sinjalizon qe do te ndodh diqka
        self.order_table.bind(on_row_press=self.on_row_press) 
            
        return self.screen
    
    #krijimi i metodave te reja
    def on_row_press(self, instance_table, instance_row):  
        # merrni numrin 'real' të rreshtit duke e ndarë indeksin e rreshtit me të dhënat e kolonës së tabelës së shembullit
        # Hint: the instance_row.index is always counted based on column data
        row_number = int(instance_row.index/len(instance_table.column_data))
        self.__selected_product = instance_table.row_data[row_number]
        
    # Metoda për shtimin e produktit të zgjedhur në tabelën e porosive
    def add_to_order(self, instance):
        if self.__selected_product is None:
            return
        quantity = self.quantity_input.text
        size = self.spinner.text
        
        if quantity and size:  
            product_data = [
                self.__selected_product[0],
                self.__selected_product[1],
                self.__selected_product[2],
                quantity,
                size
            ]
            self.order_table.row_data.append(product_data)
            self.order_table.update_row_data
        
        self.__selected_product = None  
        self.quantity_input.text = " "  
        self.spinner.text = "Select Size" 
        
    #Metodë për fshirjen e produktit të përzgjedhur nga tabela e porosive
    def delete_from_order(self, instance):
        if self.__selected_product is None:
            return 
        
        selected_row = None
        for row in self.order_table.row_data:
            if row[0] == self.__selected_product[0] and row[1] == self.__selected_product[1]:
                selected_row = row
                break  #  break e ndal iterimin e for loopes me lart
        
        if selected_row:
            self.order_table.row_data.remove(selected_row)  #ky if na ndihmon qe produktin e selektuar ta fshijme me butonin e delete nga porosia
            self.order_table.update_row    
            
    #Metoda për rifreskimin e fushave të rendit dhe hyrjes
    def refresh(self, instance):
        self.order_table.row_data = []  
        self.quantity_input.text = " "
        self.spinner.text = "Select Size"
        self.name_field.text = " "  
        self.phone_field.text = " "
        self.invoice_label.text = "Invoice will be printed here"
        
        
    #Metodë për llogaritjen e shumës së porosisë dhe gjenerimin e një faturë 
    def calculate_amount(self, instance):
        restaurant = Restaurant("Strawbarry" , "Rruga Ahmet Kaqiku")
        name = self.name_field.text  
        phone_number = self.phone_field.text 
        client = Client(name, phone_number) 
       
        order_calculator = OrderCalculatorKS() if self.check_box_ks.active else OrderCalculatorGER() 
        order = Order()
        order_manager = OrderManager() 
        
        #U shtua porosia me produkte nga tabelat e porosive
        for product in self.order_table.row_data:
            product_id = int(product[0])  
            product_name = str(product[1])
            price = float(product[2])
            quantity = float(product[3])
            size = self._get_size(str(product[4]))
            # Qka do te ndodh nese ne e paraqesim nje produkt?
            ordered_product = Product(product_name, product_id, price)
            order_manager.add_order_item(order, ordered_product, quantity, size )#pjesa ku i shtojme(klikojme) produktet per ti porositur
        order_amount = order_calculator.calculate_order_amount(order)
        order_printer = InvoiceBuilder()
        invoice = order_printer.get_order_info(restaurant, client, order, order_amount, order_calculator.get_vat_rate(False))
        #percaktimi i tekstit te fatures per ta kalkuluar faturen
        self.invoice_label.text = invoice
        
        #Përcaktoni një metodë private që konverton një paraqitje të vargut të madhësisë së artikullit të rendit
    def _get_size(self, order_item_size):
        match order_item_size:
            case "Small":
                return OrderItemSize.SMALL
            case "Medium":
                return OrderItemSize.MEDIUM
            case "Large":
                return OrderItemSize.LARGE
            case "XXL":
                return OrderItemSize.XXL
            case _:
                print("No valid order_item_size" + order_item_size)
                return 1
            
RestaurantApp().run()