import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date

# Function to validate PNR and password
def validate_pnr(pnr, password):
    try:
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="jiggistyle",
            database="railway"
        ) as db:
            cursor = db.cursor()
            query = "SELECT * FROM passengers WHERE pnr = %s AND password = %s"
            cursor.execute(query, (pnr, password))
            return cursor.fetchone()
    except Error as err:
        st.error(f"Database error: {err}")
        return None

# Function to update booking details in the database
def update_booking_in_db(pnr, new_train_no, new_travel_date):
    try:
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="jiggistyle",
            database="railway"
        ) as db:
            cursor = db.cursor()
            update_query = """
            UPDATE passengers
            SET train_no = %s, travel_date = %s
            WHERE pnr = %s
            """
            cursor.execute(update_query, (new_train_no, new_travel_date, pnr))
            db.commit()
    except Error as err:
        st.error(f"Database error: {err}")

# Main function to modify tickets
def modify_ticket():
    st.header("Modify Your Ticket")
    
    # User inputs for PNR and password
    pnr = st.text_input("Enter your PNR")
    password = st.text_input("Enter your password", type="password")
    
    if st.button("Validate PNR"):
        if not pnr or not password:
            st.error("Please enter both PNR and password.")
            return

        passenger = validate_pnr(pnr, password)
        if not passenger:
            st.error("Invalid PNR or password.")
            return
        
        st.success("PNR and password validated!")
        st.write(f"**Current Train No:** {passenger[5]}")
        st.write(f"**Current Travel Date:** {passenger[11]}")

        # Debug print to check the format of passenger[11]
        st.write(f"Debug: Current travel date value: {passenger[11]}")

        # Ensure the travel date is in the correct format
        try:
            # Convert passenger[11] to a datetime.date object if it's a string
            if isinstance(passenger[11], str):
                current_travel_date = datetime.strptime(passenger[11], "%Y-%m-%d").date()
            elif isinstance(passenger[11], datetime):
                current_travel_date = passenger[11].date()  # If it's already a datetime object
            else:
                st.error("Unexpected format for travel date.")
                return
        except ValueError:
            st.error("Invalid date format for travel date.")
            return
        
        # Select a new travel date
        new_train_no = st.text_input("Enter a new train number:", value=passenger[5])
        new_travel_date = st.date_input("Select a new travel date:", value=current_travel_date)

        if st.button("Update Booking"):
            if new_travel_date < date.today():
                st.error("Travel date cannot be in the past.")
                return

            update_booking_in_db(pnr, new_train_no, new_travel_date)
            st.success("Booking updated successfully!")
