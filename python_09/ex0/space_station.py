import datetime
from pydantic import BaseModel, Field

class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: DateTime
    is_operational:bool = Field(default=True)
    notes: str = Field(max_length=200)


def main() -> None:
    print(
        "Space Station Data Validation\n"
        "========================================\n"
    )
    try:
        valid = SpaceStation(
            station_id = "ISS001",
            name = "International Space Station",
            crew_size = 6,
            power_level = 85.5,
            oxygen_level = 92.3,
            is_operational = True
        )
        print(
            "Valid station created:"
            f"ID: {valid.station_id}"
            f"Name: {valid.name}"
            f"Crew: {valid.crew_size} people"
            f"Power: {valid.power_level}%"
            f"Oxygen: {valid.oxygen_level}%"
            if valid.is_operational:
                print("Status: Operational")
            else:
                print("Status: Non-operational")
        )
    except ValueError as e:
        print(e)

    print(
        "========================================\n"
        "Expected validation error:\n"
    )
    try:
        valid = SpaceStation(
            station_id = "ISS001",
            name = "International Space Station",
            crew_size = 21,
            power_level = 85.5,
            oxygen_level = 92.3,
            is_operational = True
        )
        print(
            "Valid station created:"
            f"ID: {valid.station_id}"
            f"Name: {valid.name}"
            f"Crew: {valid.crew_size} people"
            f"Power: {valid.power_level}%"
            f"Oxygen: {valid.oxygen_level}%"
            if valid.is_operational:
                print("Status: Operational")
            else:
                print("Status: Non-operational")
        )
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
