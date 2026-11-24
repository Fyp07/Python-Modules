from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    is_valid: bool = any(
        ingredient in ingredients.lower()
        for ingredient in allowed)
    status: str = "VALID" if is_valid else "INVALID"

    return f"({ingredients} - {status})"
