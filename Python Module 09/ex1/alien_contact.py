from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional
from typing_extensions import Self


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validator(self) -> Self:

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength >= 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def display(alien: AlienContact) -> None:
    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type}")
    print(f"Location: {alien.location}")
    print(f"Signal: {alien.signal_strength:.2f}/10")
    print(f"Duration: {alien.duration_minutes} minutes")
    print(f"Witnesses: {alien.witness_count}")
    if alien.message_received is not None:
        print(f"Message: {alien.message_received}")


def main() -> None:

    print("Alien Contact Log Validation")

    try:
        alien = AlienContact(
                contact_id="AC_2024_001",
                timestamp=datetime(2001, 12, 3),
                contact_type=ContactType.RADIO,
                location="Area 51, Nevada",
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=5,
                message_received="Greetings from Zeta Reticuli",
                is_verified=False
            )
    except ValidationError as e:
        print("Expected validation error:\n")
        for error in e.errors():
            print(error["msg"])

    try:
        print("=" * 35)
        print("Valid contact report:")
        display(alien)
        print("\n" + "=" * 35)

        alien2 = AlienContact(
                contact_id="BC_2024_001",
                timestamp=datetime(2001, 12, 3),
                contact_type=ContactType.RADIO,
                location="Area 51, Nevada",
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=5,
                message_received="Greetings from Zeta Reticuli",
                is_verified=False
            )

        display(alien2)

    except ValidationError as e:
        print("Expected validation error:\n")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
