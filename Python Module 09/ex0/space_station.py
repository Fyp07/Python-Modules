from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def display_valid(space_station: SpaceStation) -> None:

    print("=" * 35)
    print("Valid station created:")
    print(f"ID: {space_station.station_id}")
    print(f"Name: {space_station.name}")
    print(f"Crew: {space_station.crew_size} people")
    print(f"Power: {space_station.power_level:.2f}%")
    print(f"Oxygen: {space_station.oxygen_level:.2f}%")
    print("Status: ", end="")
    if not space_station.is_operational:
        print("Non ")
    print("Operational")
    print("\n" + "=" * 35)


def main() -> None:

    print("Space Station Data Validation")

    try:
        # Creating valid station
        space_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2000, 9, 21),
            is_operational=True,
        )

        # display station info
        display_valid(space_station)

        # Creating invalid station
        SpaceStation(
            station_id="AL1D02",
            name="Invalid Space Station",
            crew_size=23,  # The max size is 20
            power_level=59.2,
            oxygen_level=77.4,
            last_maintenance=datetime(2004, 12, 28),
            is_operational=False
        )

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
