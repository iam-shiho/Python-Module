from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool | None = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print(
        "Space Station Data Validation\n"
        "========================================"
    )
    try:
        valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True
        )
        print(
            "Valid station created:\n"
            f"ID: {valid.station_id}\n"
            f"Name: {valid.name}\n"
            f"Crew: {valid.crew_size} people\n"
            f"Power: {valid.power_level}%\n"
            f"Oxygen: {valid.oxygen_level}%"
        )
        if valid.is_operational:
            print("Status: Operational\n")
        else:
            print("Status: Non-operational\n")
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])

    print(
        "========================================\n"
        "Expected validation error:"
    )
    try:
        valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True
        )
        print(
            "Valid station created:"
            f"ID: {valid.station_id}"
            f"Name: {valid.name}"
            f"Crew: {valid.crew_size} people"
            f"Power: {valid.power_level}%"
            f"Oxygen: {valid.oxygen_level}%"
        )
        if valid.is_operational:
            print("Status: Operational")
        else:
            print("Status: Non-operational")
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
