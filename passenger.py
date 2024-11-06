import random
import re
import math
from data import cities, train_details, class_cost_per_km, class_details, food_menu

class Passenger:
    def __init__(self, name, age, gender, phone_no, train_no, travel_class, from_station, to_station, food_items):
        self.name = self.validate_name(name)
        self.age = self.validate_age(age)
        self.gender = self.validate_gender(gender)
        self.phone_no = self.validate_phone_no(phone_no)
        self.train_no = self.validate_train_no(train_no)
        self.train_name = train_details[self.train_no]
        self.travel_class = self.validate_travel_class(travel_class)
        self.from_station = from_station
        self.to_station = to_station
        self.distance = self.calculate_distance(from_station, to_station)
        self.pnr, self.seat_number = self.generate_pnr_and_seat()
        self.password = self.generate_password()
        self.status = "confirmed"
        self.amount = self.calculate_ticket_cost() + sum(food_menu[item] for item in food_items)
        self.food_items = food_items
        self.coach = self.generate_coach()

    def validate_name(self, name):
        pattern_for_name = r"^[a-zA-Z\s]+$"
        if re.match(pattern_for_name, name):
            return name
        else:
            raise ValueError("\nEnter a valid name.")

    def validate_age(self, age):
        pattern_for_age = r"^[1-9][0-9]?$|^1[0-1][0-9]?$|^12[0-7]?$"
        if re.match(pattern_for_age, str(age)):
            return age
        else:
            raise ValueError("\nEnter a valid age.")

    def validate_gender(self, gender):
        if gender in ["male", "female", "other"]:
            return gender
        else:
            raise ValueError("\nEnter a valid gender.")

    def validate_phone_no(self, phone_no):
        pattern_for_phone_no = r"^(7|8|9)[0-9]{9}$"
        if re.match(pattern_for_phone_no, phone_no):
            return phone_no
        else:
            raise ValueError("\nEnter a valid phone number.")

    def validate_train_no(self, train_no):
        if train_no in train_details:
            return train_no
        else:
            raise ValueError("\nInvalid train number.")

    def validate_travel_class(self, travel_class):
        if travel_class in class_details:
            return travel_class
        else:
            raise ValueError("\nInvalid travel class.")

    def calculate_distance(self, from_station, to_station):
        if from_station.lower() not in cities or to_station.lower() not in cities:
            raise ValueError("\nInvalid departure station or arival station.")

        from_distance = cities[from_station.lower()]
        to_distance = cities[to_station.lower()]

        return abs(math.sqrt(from_distance**2 + to_distance**2))

    def calculate_ticket_cost(self):
        class_name = class_details[self.travel_class]
        cost_per_km = class_cost_per_km[class_name]
        return self.distance * cost_per_km

    def generate_password(self):
        return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

    def generate_pnr_and_seat(self):
        pnr = random.randint(100000, 999999)
        seat_number = random.randint(1, 60)
        return pnr, seat_number

    def generate_coach(self):
        coach_alphabet = random.choice(["A", "B", "C"])
        coach_number = random.randint(1, 4)
        return f"{coach_alphabet}{coach_number}"

    def get_details(self):
        food_items_str = ", ".join(self.food_items)
        return (f"PNR: {self.pnr}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Phone No: {self.phone_no}, Train No: {self.train_no}, Train Name: {self.train_name}, "
                f"Class: {class_details[self.travel_class]}, From: {self.from_station}, To: {self.to_station},Coach: {self.coach}"
                f"Seat Number: {self.seat_number},Food Items: {food_items_str}, Status: {self.status}, Amount: ₹{self.amount:.2f}")
