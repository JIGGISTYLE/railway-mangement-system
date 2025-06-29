import random
import qrcode
import streamlit as st
from io import BytesIO
from datetime import datetime, timedelta
from passenger import Passenger, save_passenger_to_db
from data import cities, train_details, class_details, food_menu
from fpdf import FPDF
import os
import tempfile

today = datetime.today()

def generate_qr_code(ticket_info):
    qr = qrcode.make(ticket_info)
    img = BytesIO()   # for buffer image
    qr.save(img, 'PNG')     
    img.seek(0)  # Reset the buffer position to the start
    return img

def generate_ticket_pdf(passenger, train_details, class_details, food_menu):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 24)
    pdf.set_fill_color(255, 140, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 15, "TRAIN TICKET", 0, 1, 'C', fill=True)

    pdf.set_font("Arial", "", 16)
    pdf.cell(0, 10, "ECONOMY CLASS", 0, 1, 'C')

    pdf.ln(10)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "B", 12)

    details = [
        ("Name of Passenger", passenger.name),
        ("From", passenger.from_station.capitalize()),
        ("To", passenger.to_station.capitalize()),
        ("Train No", str(passenger.train_no)),
        ("Date", passenger.travel_date.strftime('%d-%m-%Y')),
        ("Departure", passenger.departure_time.strftime('%I:%M %p')),
        ("Coach", passenger.coach),
        ("Seat No", str(passenger.seat_number)),
        ("Class", class_details.get(passenger.travel_class, "Unknown")),
        ("Food Items", ", ".join(passenger.food_items) if passenger.food_items else "None"),
        ("Amount Paid", f"INR {passenger.amount:.2f}")
    ]

    col_widths = [60, 100]
    row_height = 8
    for label, value in details:
        pdf.cell(col_widths[0], row_height, label, border=1)
        pdf.cell(col_widths[1], row_height, value, border=1, ln=1)

    if passenger.qr_code_image:
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_file.write(passenger.qr_code_image.getvalue())
            temp_file_path = temp_file.name
        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "QR Code:", 0, 1, 'L')
        pdf.image(temp_file_path, x=90, y=pdf.get_y(), w=30, h=30)
        os.remove(temp_file_path)

    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest='S').encode('latin1'))
    pdf_output.seek(0)
    return pdf_output

def finish_booking():
    name = st.session_state.get("name", "")
    age = st.session_state.get("age", 0)
    gender = st.session_state.get("gender", "")
    phone_no = st.session_state.get("phone_no", "")
    from_station = st.session_state.get("from_station", "")
    to_station = st.session_state.get("to_station", "")
    travel_class = st.session_state.get("travel_class", "")
    selected_train = st.session_state.get("selected_train", "")
    food_items = st.session_state.get("food_items", [])
    travel_date = st.session_state.get("travel_date", "")

    if not name or not age or not phone_no or not from_station or not to_station or not travel_class or not selected_train:
        st.error("Please fill all the fields.")
    elif not Passenger.validate_phone_number(phone_no):
        st.error("Invalid phone number format!")
    else:
        try:
            train_no = int(selected_train.split(" - ")[0])
            passenger = Passenger(
                name, age, gender, phone_no, train_no, travel_class,
                from_station, to_station, food_items, travel_date,
                st.session_state.departure_times[train_no]
            )
            st.session_state.passenger_list.append(passenger)
            st.session_state.total_amount += passenger.amount
            st.session_state.passenger_count += 1

            save_passenger_to_db(passenger)

            st.session_state.passenger = passenger
            st.session_state.booking_complete = True

            qr_info = (
                f"PNR: {st.session_state.passenger.pnr}, "
                f"Name: {st.session_state.passenger.name}, "
                f"Train: {train_details[st.session_state.passenger.train_no]}, "
                f"Seat: {st.session_state.passenger.seat_number}, "
                f"Class: {class_details[st.session_state.passenger.travel_class]}"
            )
            st.session_state.qr_code_img = generate_qr_code(qr_info)
            st.session_state.pdf_file = generate_ticket_pdf(
                st.session_state.passenger, train_details, class_details, food_menu
            )
        except ValueError as e:
            st.error(f"Error processing booking: {str(e)}")

def book_ticket():
    st.subheader("Book a Ticket")

    if "total_amount" not in st.session_state:
        st.session_state.total_amount = 0
    if "passenger_count" not in st.session_state:
        st.session_state.passenger_count = 0
    if "passenger_list" not in st.session_state:
        st.session_state.passenger_list = []
    if "qr_code_img" not in st.session_state:
        st.session_state.qr_code_img = None
    if "pdf_file" not in st.session_state:
        st.session_state.pdf_file = None
    if "passenger" not in st.session_state:
        st.session_state.passenger = None
    if "booking_complete" not in st.session_state:
        st.session_state.booking_complete = False
    if "show_trains" not in st.session_state:
        st.session_state.show_trains = False

    if st.session_state.booking_complete:
        st.success("Booking complete!")
        st.download_button("Download Ticket PDF", st.session_state.pdf_file, file_name="ticket.pdf")
        st.image(st.session_state.qr_code_img)
        st.write(f"PNR: {st.session_state.passenger.pnr}")
        st.write(f"password: {st.session_state.passenger.password} (please keep it confidential for security)")
        return

    with st.form(key='passenger_form'):
        st.session_state.name = st.text_input("Enter passenger's name:")
        st.session_state.age = st.number_input("Enter passenger's age:", min_value=0)
        st.session_state.gender = st.selectbox("Select gender:", ["male", "female", "other"])
        st.session_state.phone_no = st.text_input("Enter mobile number:")
        st.session_state.travel_date = st.date_input(
            "Select your travel date:",
            min_value=today
        )

        st.session_state.from_station = st.selectbox("Select departure station:", options=list(cities.keys()))
        st.session_state.to_station = st.selectbox("Select arrival station:", options=list(cities.keys()))

        submit_passenger = st.form_submit_button("Submit Passenger")

    if submit_passenger:
        if st.session_state.from_station == st.session_state.to_station:
            st.error("Departure and arrival stations cannot be the same!")
        else:
            st.session_state.show_trains = True

    if st.session_state.show_trains:
        if "train_choices" not in st.session_state or not st.session_state.train_choices:
            random_trains = random.sample(list(train_details.items()), 5)
            train_choices = []
            departure_times = {}
            for number, name in random_trains:
                random_hour = random.randint(5, 23)
                random_minute = random.choice([0, 15, 30, 45])
                departure_time = (datetime.min + timedelta(hours=random_hour, minutes=random_minute)).time()
                formatted_time = departure_time.strftime("%I:%M %p")
                departure_times[number] = departure_time
                train_choices.append(f"{number} - {name} | Departure: {formatted_time}")
            st.session_state.train_choices = train_choices
            st.session_state.departure_times = departure_times

        st.session_state.selected_train = st.selectbox(
            "Select a Train:", st.session_state.train_choices
        )
        st.session_state.travel_class = st.selectbox(
            "Select a class:", [""] + list(class_details.keys()),
            format_func=lambda x: class_details[x] if x else "Choose Class"
        )
        if not st.session_state.travel_class:
            st.error("Travel class must be selected.")
            return

        st.session_state.food_items = st.multiselect(
            "Select food items (optional):",
            options=list(food_menu.keys()),
            format_func=lambda item: f"{item} - ₹{food_menu[item]}"
        )
        if st.button("Finish Booking"):
            finish_booking()
