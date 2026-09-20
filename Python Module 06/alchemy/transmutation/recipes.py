
import alchemy
from elements import create_fire

def lead_to_gold():
    return f"Recipe transmuting Lead to Gold: brew {alchemy.create_air()} and {alchemy.strength_potion()} mixed with {create_fire()}"
