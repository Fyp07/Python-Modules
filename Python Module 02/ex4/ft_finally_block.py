
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error.") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error.") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not plant_name == plant_name.capitalize():
        raise PlantError(f"Invalid plant "
                         f"name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:

    valid_plants: list[str] = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants: list[str] = ["Tomato", "lettuce", "carrots"]

    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    try:
        print("Opening watering system")
        for plant in valid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    finally:
        print("Closing watering system")

    print("\ntesting invalid plants...")
    try:
        print("Opening watering system")
        for plant in invalid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
