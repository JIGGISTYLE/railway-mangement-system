import pytest
from project import Passenger

@pytest.fixture
def passenger():
    return Passenger("John Doe", 30, "male", "9876543210", 1234, 1, "delhi", "mumbai", ["Veg Meal"])

def test_validate_name(passenger):
    # Test valid names
    assert passenger.validate_name("John Doe") == "John Doe"
    assert passenger.validate_name("Alice") == "Alice"

    # Test invalid names (should raise ValueError)
    with pytest.raises(ValueError):
        passenger.validate_name("John123")  # Contains numbers
    with pytest.raises(ValueError):
        passenger.validate_name("")  # Empty string

def test_validate_phone_no(passenger):
    # Test valid phone numbers
    assert passenger.validate_phone_no("9876543210") == "9876543210"
    assert passenger.validate_phone_no("8123456789") == "8123456789"

    # Test invalid phone numbers (should raise ValueError)
    with pytest.raises(ValueError):
        passenger.validate_phone_no("1234567890")  # Does not start with 7, 8, or 9
    with pytest.raises(ValueError):
        passenger.validate_phone_no("98765")  # Too short
    with pytest.raises(ValueError):
        passenger.validate_phone_no("98765432101")  # Too long
    with pytest.raises(ValueError):
        passenger.validate_phone_no("98765432a1")  # Contains letters

def test_validate_age(passenger):
    # Test valid ages
    assert passenger.validate_age(30) == 30
    assert passenger.validate_age(99) == 99

    # Test invalid ages (should raise ValueError)
    with pytest.raises(ValueError):
        passenger.validate_age(-1)  # Negative age
    with pytest.raises(ValueError):
        passenger.validate_age(0)  # Age zero
    with pytest.raises(ValueError):
        passenger.validate_age(150)  # Unrealistic age
    with pytest.raises(ValueError):
        passenger.validate_age("abc")  # Non-numeric input

if __name__ == "__main__":
    pytest.main()
