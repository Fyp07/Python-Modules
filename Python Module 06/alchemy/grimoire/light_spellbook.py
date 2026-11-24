from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    is_valid: str = validate_ingredients(ingredients)

    if "INVALID" in is_valid:
        return f"Spell rejected: {spell_name} {is_valid}"
    return f"Spell recorded: {spell_name} {is_valid}"
