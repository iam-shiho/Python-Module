from ..potions import strength_potion
from ..elements import create_air
import elements

def lead_to_gold() -> str:
    return "Recipe transmuting Lead to "\
        f"Gold: brew ’{create_air()}’ and "\
        f"’{strength_potion()}’ mixed with ’{elements.create_fire()}’"
