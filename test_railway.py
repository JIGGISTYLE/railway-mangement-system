import pytest
from datetime import datetime
from passenger import Passenger, save_passenger_to_db
from data import food_menu, train_details

# Sample data for testing
sample_data = {
    'name': 'John Doe',
    'age': 30,
    'gender': 'male',
    'phone_no': '9876543210',
    'train_no': 12001,  # Change this to a valid train number like 12001
    'travel_class': 'First Class',
    'from_station': 'delhi',
    'to_station': 'mumbai',
    'food_items': ['veg biryani', 'water bottle'],
    'travel_date': datetime(2024, 12, 15).date(),
    'departure_time': datetime(2024, 12, 15, 10, 30).time()
}


# Test case for initializing a passenger
def test_passenger_initialization():
    passenger = Passenger(
        name=sample_data['name'],
        age=sample_data['age'],
        gender=sample_data['gender'],
        phone_no=sample_data['phone_no'],
        train_no=sample_data['train_no'],
        travel_class=sample_data['travel_class'],
        from_station=sample_data['from_station'],
        to_station=sample_data['to_station'],
        food_items=sample_data['food_items'],
        travel_date=sample_data['travel_date'],
        departure_time=sample_data['departure_time']
    )
    
    # Assertions to check if passenger object is initialized correctly
    assert passenger.name == sample_data['name']
    assert passenger.age == sample_data['age']
    assert passenger.gender == sample_data['gender']
    assert passenger.phone_no == sample_data['phone_no']
    assert passenger.train_no == sample_data['train_no']
    assert passenger.train_name == train_details.get(sample_data['train_no'], "Unknown Train")
    assert passenger.travel_class == sample_data['travel_class']
    assert passenger.from_station == sample_data['from_station'].lower()
    assert passenger.to_station == sample_data['to_station'].lower()
    assert passenger.travel_date == sample_data['travel_date']
    assert passenger.departure_time == sample_data['departure_time']
    assert passenger.food_items == sample_data['food_items']
    assert passenger.amount == passenger.calculate_ticket_cost() + sum(food_menu.get(item, 0) for item in sample_data['food_items'])

# Test case for saving the passenger to the database
def test_finish_booking():
    # Create a Passenger object
    passenger = Passenger(
        name=sample_data['name'],
        age=sample_data['age'],
        gender=sample_data['gender'],
        phone_no=sample_data['phone_no'],
        train_no=sample_data['train_no'],
        travel_class=sample_data['travel_class'],
        from_station=sample_data['from_station'],
        to_station=sample_data['to_station'],
        food_items=sample_data['food_items'],
        travel_date=sample_data['travel_date'],
        departure_time=sample_data['departure_time']
    )
    
    # Save the passenger to the database (you can mock this in unit tests)
    save_passenger_to_db(passenger)
    
    # Assertions to check if data has been inserted (mock the DB interaction if needed)
    # For now, we just check that the passenger object was created successfully.
    assert passenger.pnr is not None
    assert passenger.seat_number is not None
    assert passenger.coach is not None
    assert passenger.qr_code_image is not None
