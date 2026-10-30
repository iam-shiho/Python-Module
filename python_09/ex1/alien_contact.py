from typing_extensions import Self
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool | None = Field(default=False)

    @model_validator(mode="after")
    def validate_contact_id(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        return self

    @model_validator(mode="after")
    def validate_physical(self) -> Self:
        if self.contact_type.value == "physical":
            if self.is_verified is False:
                raise ValueError('Physical contact reports must be verified')
        return self

    @model_validator(mode="after")
    def validate_telepathic(self) -> Self:
        if self.contact_type.value == "telepathic":
            if self.witness_count < 3:
                raise ValueError(
                    'Telepathic contact requires at least 3 witnesses'
                )
        return self

    @model_validator(mode="after")
    def validate_signal_strength(self) -> Self:
        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError(
                    'Strong signals (> 7.0) should include received messages'
                )
        return self


def demonstration() -> None:
    print(
        "Alien Contact Log Validation\n"
        "======================================"
    )
    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print(
            "Valid contact report:",
            f"ID: {valid.contact_id}",
            f"Type: {valid.contact_type.value}",
            f"Location: {valid.location}",
            f"Signal: {valid.signal_strength}/10",
            f"Duration: {valid.duration_minutes} minutes",
            f"Witnesses: {valid.witness_count}",
            f"Message: '{valid.message_received}'",
            sep="\n"
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])

    print(
        "\n======================================\n"
        "Expected validation error:"
    )
    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli"
        )
        print(
            "Valid contact report:",
            f"ID: {valid.contact_id}",
            f"Type: {valid.contact_type.value}",
            f"Location: {valid.location}",
            f"Signal: {valid.signal_strength}/10",
            f"Duration: {valid.duration_minutes} minutes",
            f"Witnesses: {valid.witness_count}",
            f"Message: '{valid.message_received}'",
            sep="\n"
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    demonstration()
