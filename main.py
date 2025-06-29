import streamlit as st
from railway import book_ticket
from modify import modify_ticket
from cancel import cancel_ticket
from about import about_project

# Page config
st.set_page_config(page_title="Railway Reservation System", layout="wide", page_icon="🚂")

# Main title
st.title("🚂 Welcome to the Railway Reservation System")
st.caption("Your one-stop solution for hassle-free train bookings, modifications, and cancellations.")

# Initialize session state for page selection
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar navigation with buttons
with st.sidebar:
    st.header("🚉 Navigation")
    st.write("Choose an option to get started:")
    
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("🎫 Book a Ticket"):
        st.session_state.page = "Book a Ticket"
    if st.button("✏️ Modify Ticket"):
        st.session_state.page = "Modify Ticket"
    if st.button("❌ Cancel Ticket"):
        st.session_state.page = "Cancel Ticket"
    if st.button("ℹ️ About"):
        st.session_state.page = "About"

    st.write("---")
    st.info("Need help? Visit the About section for detailed guidance.")

# Dynamic content for each page
if st.session_state.page == "Home":
    st.subheader("Your Journey Begins Here!")
    st.success("Welcome to a seamless experience of train ticket booking and management!")
    
    # Train emoji banner
    st.markdown(
        """
        ### 🚂🚃🚃🚃🚃 **Your Trusted Travel Partner** 🚃🚃🚃🚃🚃
        """
    )
    
    # Highlight key features
    st.write("### Key Features:")
    st.columns(2)  # Two-column layout for features
    with st.container():
        st.write("🎫 **Book a Ticket**")
        st.caption("Reserve your seat with ease and convenience.")
        
        st.write("✏️ **Modify Ticket**")
        st.caption("Update your travel details hassle-free.")
        
        st.write("❌ **Cancel Ticket**")
        st.caption("Plans changed? Cancel your booking instantly.")
        
        st.write("ℹ️ **About**")
        st.caption("Learn more about the system and its benefits.")
    
    # Interactive expander with additional details
    with st.expander("Why Choose Us?"):
        st.write("""
            - Easy-to-use platform for managing your railway reservations.
            - Transparent and secure booking process.
            - Customer-friendly features to modify or cancel tickets without hassle.
        """)
        st.info("Your comfort is our priority. Have a safe journey!")

elif st.session_state.page == "Book a Ticket":
    book_ticket()

elif st.session_state.page == "Modify Ticket":
    modify_ticket()

elif st.session_state.page == "Cancel Ticket":
    cancel_ticket()

elif st.session_state.page == "About":
    about_project()
