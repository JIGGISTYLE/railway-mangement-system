# This file contains all the data structures used in the railway reservation system

# Initialize the list to store passenger objects
passenger_list = []





cities = {
    "delhi": 0,
    "mumbai": 1400,
    "kolkata": 1500,
    "chennai": 2200,
    "bangalore": 2100,
    "hyderabad": 1700,
    "ahmedabad": 950,
    "pune": 1450,
    "jaipur": 280,
    "lucknow": 500,
    "patna": 1000,
    "bhopal": 750,
    "chandigarh": 260,
    "amritsar": 450,
    "varanasi": 800,
    "kanpur": 440,
    "nagpur": 1080,
    "surat": 1170,
    "guwahati": 1900,
    "visakhapatnam": 1900,
    "coimbatore": 2400,
    "madurai": 2500,
    "indore": 820,
    "raipur": 1220,
    "thiruvananthapuram": 2800,
    "agra": 200,
    "gwalior": 320,
    "ranchi": 1250,
    "bhubaneswar": 1700,
    "jabalpur": 800,
    "vijayawada": 1800,
    "rajkot": 1100,
    "vadodara": 980,
    "mangalore": 2350,
    "aurangabad": 1300,
    "nashik": 1220,
    "meerut": 70,
    "dehradun": 250,
    "shimla": 350,
    "jammu": 590,
    "srinagar": 820,
    "udaipur": 660,
    "ajmer": 390,
    "jodhpur": 620,
    "kota": 500,
    "allahabad": 650,
    "aligarh": 140,
    "gorakhpur": 800,
    "tiruchirappalli": 2600,
    "salem": 2300,
    "hubli": 1800,
    "mysore": 2300
}

train_details = {
    8375: "Shatabdi Express",
    1234: "Rajdhani Express",
    5678: "Duronto Express",
    9101: "Garib Rath",
    1122: "Tejas Express",
    2246: "Humsafar Express",
    3821: "Sampark Kranti Express",
    4812: "Yuva Express",
    6745: "Jan Shatabdi Express",
    9987: "Maharaja Express",
    2354: "Vande Bharat Express",
    5698: "Mahamana Express",
    4785: "Gatiman Express",
    1256: "Antyodaya Express",
    9865: "Double Decker Express",
    3142: "Intercity Express",
    7531: "Suvidha Express",
    8524: "Vivek Express",
    2698: "Kavi Guru Express",
    5423: "Rajya Rani Express"
}


class_cost_per_km = {
    "AC FIRST CLASS": 3.00,
    "AC SECOND CLASS": 2.00,
    "AC THIRD CLASS": 1.25,
    "SLEEPER CLASS": 0.50,
    "GENERAL CLASS": 0.30
}


class_details = {
    1: "AC FIRST CLASS",
    2: "AC SECOND CLASS",
    3: "AC THIRD CLASS",
    4: "SLEEPER CLASS",
    5: "GENERAL CLASS"
}


food_menu = {
    "Veg Meal": 150,
    "Non-Veg Meal": 200,
    "Snacks": 50,
    "Drinks": 30,
    "water bottle": 15
}