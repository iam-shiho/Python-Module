from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_lists = dark_spell_allowed_ingredients()
    lists = ingredients.split()
    for text in lists:
        if text.lower() in allowed_lists:
            return "VALID"
    else:
        return "INVALID"
