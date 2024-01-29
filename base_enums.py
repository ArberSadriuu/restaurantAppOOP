from enum import Enum


# krijoni një klasë të re Enum për madhësitë e artikujve të porosisë
class OrderItemSize(Enum):
    # enums to specify order item sizes
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    XXL = 4
    
# Krijoni klasë të re Enum për Vendndodhjen
class Location(Enum):
    # enums to specify Location
    KOSOVO = 1
    GERMANY = 2
    
class ApplicationMode(Enum):
    
    ORDER = 1
    TABLE_RESERVATION = 2