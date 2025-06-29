import streamlit as st
import mysql.connector
from passenger import Passenger  # Import the Passenger class

# Function to connect to the database
def connect_db():
    return mysql.connector.connect(
        host="localhost",  # Database server address
        user="root",       # Database username
        password="jiggistyle",  # Database password
        database="railway"  # Database name
    )

# Function to fetch ticket details by PNR and password
def get_ticket_details(pnr, password):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM passengers WHERE pnr = %s AND password = %s"
    cursor.execute(query, (pnr, password))
    result = cursor.fetchone()
    db.close()
    return result

# Function to cancel the ticket
def cancel_ticket():
    st.header("Cancel Your Ticket")
    
    # PNR and Password input to identify the ticket
    pnr = st.text_input("Enter your PNR to cancel")
    password = st.text_input("Enter your password:", type="password")
    
    if pnr and password:
        # Fetch ticket details for the given PNR and password
        ticket = get_ticket_details(pnr, password)
        
        if ticket:
            # Show ticket details (removed train_name)
            st.write(f"Ticket Details: \nPNR: {ticket.get('pnr', 'N/A')} \nDeparture: {ticket.get('departure', 'Not Available')} \nArrival: {ticket.get('arrival', 'Not Available')}")
            
            # Show refund warning
            st.warning("Refund of 18% will be deducted upon cancellation.")
            
            # Ask user for confirmation
            cancel_confirm = st.radio("Do you want to proceed with the cancellation?", ["Yes", "No"])
            
            if cancel_confirm == "Yes":
                try:
                    # Connect to the database to cancel the ticket
                    db = connect_db()
                    cursor = db.cursor()
                    
                    # SQL query to update the status of the ticket to "cancelled"
                    update_query = "UPDATE passengers SET status = 'cancelled' WHERE pnr = %s"
                    cursor.execute(update_query, (pnr,))
                    db.commit()

                    # Check if any rows were affected (ticket found and updated)
                    if cursor.rowcount > 0:
                        refund_amount = ticket.get('ticket_cost', 0) * 0.18
                        total_refund = ticket.get('ticket_cost', 0) - refund_amount
                        st.success(f"Ticket cancelled successfully! Refund Amount: ₹{total_refund}")
                        st.write("Thank you for using our service!")
                    else:
                        st.error("No ticket found with the provided PNR. Please check the PNR and try again.")
                except mysql.connector.Error as err:
                    st.error(f"Error: {err}")
                finally:
                    db.close()  # Close the database connection
            else:
                st.write("Ticket cancellation aborted.")
        else:
            st.error("Invalid PNR or password. Please try again.")
