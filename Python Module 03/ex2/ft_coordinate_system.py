
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            player_pos: list[str] = str(input(
                "Enter new coordinates as floats in format 'x, y, z': ")
                ).strip(" ").split(",")

            coordinates: list = []

            for number in player_pos:
                coordinates.append(float(number))

            if len(coordinates) != 3:
                raise SyntaxError("The program only accepts 3 numbers.")

            x: float = coordinates[0]
            y: float = coordinates[1]
            z: float = coordinates[2]

            return x, y, z

        except ValueError as e:
            print(f"Invalid value -> {e}")
        except SyntaxError as e:
            print(f"Invalid syntax -> {e}")


def main() -> None:
    pos: tuple[float, float, float] = get_player_pos()
    x1: float = pos[0]
    y1: float = pos[1]
    z1: float = pos[2]
    to_center: float = math.sqrt((x1**2) + (y1**2) + (z1**2))

    print("=== Game Coordinate, System ===")
    print("\nGet a first set of coordinates")
    print(f"Got a first tuple: {pos}")
    print(f"It includes: X = {x1}, Y = {y1}, Z = {z1}")
    print(f"Distance to center: {to_center:.4f}")

    print("\nGet a second set of coordinates")
    new_pos: tuple[float, float, float] = get_player_pos()
    x2: float = new_pos[0]
    y2: float = new_pos[1]
    z2: float = new_pos[2]
    distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2))
    print(f"Distance between 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    main()
