# import Meal and Drink class from BaseModel
from base_model import Meal, Drink, Menu
import csv
from custom_exceptions import InvalidMenuFile

class MenuPrinter:
    def print_menu(self, menu):
        menu_items = menu.get_menu_items()
        for key in menu_items:
            product = menu_items[key]
            # duke prezantuar një shembull për të kontrolluar llojin e objektit
            if(isinstance(product, Meal)):
                # përgatit discription text nëse është i disponueshëm
                description_text = "" if product.get_description() == "" else " (" + product.get_description() + ")"
                print(str(product.get_product_id()) + " . " + product.get_name() + description_text + " | " + str(product.get_price()) + " Euro ")
            elif(isinstance(product, Drink)):
                # duke prezantuar 'ternary operator' për të përgatitur sugarfree text
                sugar_free_text = "yes" if product.is_sugar_free() else "no"
                print(str(product.get_product_id()) + " . " + product.get_name() + " (Sugar free: " + sugar_free_text + ") | " + str(product.get_price()) + " Euro ")
                
# Sherben per importimin e menyse nga file
class MenuImporter:
    
    def import_menu(self, file_path):
        #përdor metodën open() për të importuar menunë
        menu_file = open(file_path)
        #created new atribute file path
        csv_reader = csv.reader(menu_file)
        
        return self._transform_csv_menu_data_to_menu(csv_reader)
    
    def _transform_csv_menu_data_to_menu(self, csv_reader):
        imported_menu = Menu(True)
        for row in csv_reader:
            #lexo të dhënat nga array
            product_id = int(row[0])
            product_name = row[1]
            product_price = float(row[2])
            product_category = row[3]
            
        #iteroni përmes kategorive të vakteve dhe pijeve
            if "meal" == product_category:
                product = Meal(product_id, product_name, product_price, "")
            elif "drink" == product_category:
                #shtimi i sugar_free, specifikisht për pije
                sugar_free = row[4]
                product = Drink(product_id, product_name, product_price, sugar_free)
            else:
                exception_message = "".join("The menu field couldn't be processed as a product category from product").join(product_name).join("is invalid.")
                raise InvalidMenuFile(exception_message)
            
            imported_menu.get_menu_items().update({product_id:product})
            
        return imported_menu
            