from typing_extensions import Self
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class CrewRanks(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember]
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_missionid(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        return self

    @model_validator(mode="after")
    def validate_rank(self) -> Self:
        for crew_1 in self.crew:
            if crew_1.rank.value in ("commander", "captain"):
                return self
        raise ValueError('Mission must have at least one Commander or Captain')

    @model_validator(mode="after")
    def validate_experience(self) -> Self:
        ex_count = 0
        if self.duration_days > 365:
            for crew_1 in self.crew:
                if crew_1.years_experience >= 5:
                    ex_count += 1
            if (len(self.crew)/2) > ex_count:
                raise ValueError(
                    'Long missions (> 365 days) need 50% '
                    'experienced crew (5+ years)'
                )
        return self

    @model_validator(mode="after")
    def validate_active(self) -> Self:
        for crew_1 in self.crew:
            if not crew_1.is_active:
                raise ValueError('All crew members must be active')
        return self


def demonstration() -> None:
    print(
        "Space Mission Crew Validation\n"
        "========================================="
    )
    try:
        validate = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                 member_id="sarah",
                 name="Sarah Connor",
                 rank=CrewRanks.COMMANDER,
                 age=70,
                 specialization="Mission Command",
                 years_experience=6,
                ),
                CrewMember(
                 member_id="john",
                 name="John Smith",
                 rank=CrewRanks.LIEUTENANT,
                 age=70,
                 specialization="Navigation",
                 years_experience=6,
                ),
                CrewMember(
                 member_id="alice",
                 name="Alice Johnson",
                 rank=CrewRanks.OFFICER,
                 age=70,
                 specialization="Engineering",
                 years_experience=6,
                )
            ],
            budget_millions=2500.0
        )

        print(
            "Valid mission created:",
            f"Mission: {validate.mission_name}",
            f"ID: {validate.mission_id}",
            f"Destination: {validate.destination}",
            f"Duration: {validate.duration_days} days",
            f"Budget: ${validate.budget_millions}M",
            f"Crew size: {len(validate.crew)}",
            "Crew members:",
            sep="\n"
        )
        for crew_1 in validate.crew:
            print(
                f"- {crew_1.name} ({crew_1.rank.value}) - "
                f"{crew_1.specialization}"
            )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])

    print(
        "=========================================\n"
        "Expected validation error:"
    )
    try:
        validate = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                 member_id="sarah",
                 name="Sarah Connor",
                 rank=CrewRanks.CADET,
                 age=70,
                 specialization="Mission Command",
                 years_experience=6,
                ),
                CrewMember(
                 member_id="john",
                 name="John Smith",
                 rank=CrewRanks.LIEUTENANT,
                 age=70,
                 specialization="Navigation",
                 years_experience=6,
                ),
                CrewMember(
                 member_id="alice",
                 name="Alice Johnson",
                 rank=CrewRanks.OFFICER,
                 age=70,
                 specialization="Engineering",
                 years_experience=6,
                )
            ],
            budget_millions=2500.0
        )

        print(
            "Valid mission created:",
            f"Mission: {validate.mission_name}",
            f"ID: {validate.mission_id}",
            f"Destination: {validate.destination}",
            f"Duration: {validate.duration_days} days",
            f"Budget: ${validate.budget_millions}M",
            f"Crew size: {len(validate.crew)}",
            "Crew members:",
            sep="\n"
        )
        for crew_1 in validate.crew:
            print(
                f"- {crew_1.name} ({crew_1.rank.value}) - "
                f"{crew_1.specialization}"
            )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    demonstration()
