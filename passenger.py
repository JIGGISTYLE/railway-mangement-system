import mysql.connector
import re
import random
from datetime import datetime
from data import cities, train_details, class_cost_per_km, class_details, food_menu
import qrcode
import math
from io import BytesIO


class Passenger:
    def __init__(self, name, age, gender, phone_no, train_no, travel_class, from_station, to_station, food_items, travel_date, departure_time):
        self.name = self.validate_name(name)
        self.age = self.validate_age(age)
        self.gender = self.validate_gender(gender)
        self.phone_no = self.validate_phone_number(phone_no)
        self.train_no = self.validate_train_no(train_no)
        self.train_name = train_details.get(self.train_no, "Unknown Train")
        self.travel_class = self.validate_travel_class(travel_class)
        self.from_station = from_station.lower()
        self.to_station = to_station.lower()
        self.travel_date = travel_date  # Ensure travel_date is a datetime.date object
        self.departure_time = departure_time  # Ensure departure_time is passed as a datetime.time object
        self.distance = self.calculate_distance(self.from_station, self.to_station)
        self.pnr, self.seat_number = self.generate_pnr_and_seat()
        self.password = self.generate_password()
        self.status = "confirmed"
        self.food_items = food_items
        self.amount = self.calculate_ticket_cost() + sum(food_menu.get(item, 0) for item in food_items)
        self.coach = self.generate_coach()
        self.generate_qr_code()

    @staticmethod
    def validate_name(name):
        if not name:
            raise ValueError("Name is required.")
        if re.match(r"^[a-zA-Z\s]+$", name):
            return name
        raise ValueError("Invalid name. Please enter a valid name.")

    @staticmethod
    def validate_age(age):
        age_str = str(age)
        if not age_str:
            raise ValueError("Age is required.")
        if re.match(r"^[1-9][0-9]?$|^1[0-1][0-9]?$|^12[0-7]?$", age_str):
            return int(age_str)
        raise ValueError("Invalid age. Please enter a valid age (1-127).")

    @staticmethod
    def validate_gender(gender):
        gender = gender.strip().lower()
        if gender in ["male", "female", "other"]:
            return gender
        raise ValueError("Invalid gender. Please enter 'male', 'female', or 'other'.")

    @staticmethod
    def validate_phone_number(phone_no):
        if not phone_no:
            raise ValueError("Phone number is required.")
        if re.match(r"^(6|7|8|9)[0-9]{9}$", phone_no):
            return phone_no
        raise ValueError("Invalid phone number. Please enter a valid 10-digit phone number starting with 6, 7, 8, or 9.")

    @staticmethod
    def validate_train_no(train_no):
        if train_no in train_details:
            return train_no
        raise ValueError("Invalid train number. Please enter a valid train number.")

    @staticmethod
    def validate_travel_class(travel_class):
        if travel_class in class_details:
            return travel_class
        raise ValueError("Invalid travel class. Please select a valid class.")

    @staticmethod
    def calculate_distance(from_station, to_station):
        if from_station not in cities or to_station not in cities:
            raise ValueError("Invalid departure or arrival station.")
        
        # Fetch values from cities and apply the formula
        from_distance = cities[from_station]
        to_distance = cities[to_station]
        distance = math.sqrt(from_distance ** 2 + to_distance ** 2)
        return distance

    def calculate_ticket_cost(self):
        class_name = class_details.get(self.travel_class, "Economy")
        cost_per_km = class_cost_per_km.get(class_name, 0)
        ticket_cost = self.distance * cost_per_km
        return ticket_cost

    def generate_password(self):
        return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

    def generate_pnr_and_seat(self):
        return random.randint(100000, 999999), random.randint(1, 60)

    def generate_coach(self):
        return f"{random.choice(['A', 'B', 'C'])}{random.randint(1, 4)}"

    def generate_qr_code(self):
        qr_data = f"PNR: {self.pnr}\nName: {self.name}\nTrain No: {self.train_no}\nSeat No: {self.seat_number}"
        qr = qrcode.make(qr_data)
        qr_code_img = BytesIO()
        qr.save(qr_code_img, format="PNG")
        qr_code_img.seek(0)
        self.qr_code_image = qr_code_img

def save_passenger_to_db(passenger):
    db = None  # Initialize db to None
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jiggistyle",  # Replace with your actual password
            database="railway"
        )

        if db.is_connected():
            cursor = db.cursor()

            query = """
INSERT INTO passengers (
    name, age, gender, phone_no, train_no, from_station, to_station, 
    travel_class, food_items, pnr, status, ticket_cost, travel_date, 
    departure_time, password
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

            food_items_str = ','.join(passenger.food_items) if passenger.food_items else " "
            travel_date_str = passenger.travel_date.strftime("%Y-%m-%d")
            departure_time_str = passenger.departure_time.strftime("%H:%M:%S")

            values = (
                passenger.name, passenger.age, passenger.gender, passenger.phone_no, 
                passenger.train_no, passenger.from_station, passenger.to_station, 
                passenger.travel_class, food_items_str, passenger.pnr, 
                passenger.status, passenger.amount, travel_date_str, 
                departure_time_str, passenger.password
            )

            # Execute the query
            cursor.execute(query, values)
            db.commit()
            print("Passenger saved successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if db and db.is_connected():
            cursor.close()
            db.close()
