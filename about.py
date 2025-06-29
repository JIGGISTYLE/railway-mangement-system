# about.py
import streamlit as st

def about_project():
    st.title("ℹ️ About the Railway Reservation System")
    st.write("---")
    
    # Highlighted introductory section
    st.subheader("Welcome to the Railway Reservation System!")
    st.markdown(
        """
        Our system is designed to provide a seamless and efficient platform for managing your railway bookings. Whether you're reserving tickets, modifying existing reservations, or canceling them, we've got you covered!
        """
    )
    
    # Key features section with icons
    st.write("### 🚀 Key Features:")
    st.markdown(
        """
        - 🎫 **Book Tickets**: Quickly and securely reserve your train seats.
        - ✏️ **Modify Bookings**: Update your travel details without hassle.
        - ❌ **Cancel Tickets**: Cancel your reservations with ease.
        - 🔍 **Check PNR Status**: Stay updated on your ticket status anytime.
        - ℹ️ **Learn More**: Get detailed guidance on how to use the system.
        """
    )
    
    
    
    # Why choose us section
    st.write("---")
    st.write("### 🌟 Why Choose Us?")
    st.markdown(
        """
        - ✅ **User-Friendly Interface**: Navigate with ease.
        - ✅ **Transparent Pricing**: No hidden charges.
        - ✅ **24/7 Support**: We’re here to assist you anytime.
        """
    )
    st.success("Your comfort and convenience are our top priorities!")

    # Footer section with a call to action
    st.write("---")
    st.info(
        "Ready to start your journey? Navigate to the **Home** section and begin your hassle-free railway reservation experience today!"
    )
