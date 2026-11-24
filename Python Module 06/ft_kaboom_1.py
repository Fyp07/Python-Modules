def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        print(f"{dark_spell_record('Fantasy', 'bats')}")
    except ImportError:
        print("[ERROR] Circular import detected.")


if __name__ == "__main__":
    main()
