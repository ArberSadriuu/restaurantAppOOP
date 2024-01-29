#krijoi klasën e re të kontrolluesit për operacionet e vendndodhjes
from base_enums import Location
class LocationManager:
    
    # shtimi @staticmethod për të shënuar metodën si statike
    @staticmethod
    def get_location_from_id(location_id):
            for location in Location:
                if location.value == location_id:
                    return location
           
            raise Exception("No location could be found for given location parameter.")
            