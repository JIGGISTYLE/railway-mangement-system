# Railway Reservation System


#### Video Demo: (https://youtu.be/rtvYWEeOT6E)

#### Description:

This project is a Railway Reservation System implemented in Python. It allows users to book train tickets, check PNR status, cancel tickets, and modify bookings. The system is designed to be user-friendly and efficient, simulating a real-world railway reservation process.

### Project Structure

The project consists of three main Python files:

1. `project.py`: This is the main file that contains the user interface and core functionality of the reservation system. It includes functions for displaying the menu, booking tickets, checking PNR status, cancelling tickets, and modifying bookings.

2. `passenger.py`: This file defines the Passenger class, which represents a passenger in the system. It includes methods for validating passenger details, calculating ticket costs, and generating unique identifiers like PNR and seat numbers.

3. `data.py`: This file contains all the static data used in the project, such as the list of cities, train details, class types, and food menu. It also initializes the passenger_list that stores all booked passengers.

### Key Features

1. **Ticket Booking**: Users can book tickets by providing passenger details, selecting a train, and choosing a travel class. The system calculates the ticket cost based on the distance and class type.

2. **PNR Status Check**: Passengers can check their booking status using their PNR number and password.

3. **Ticket Cancellation**: The system allows users to cancel their bookings, with a simulated refund process.

4. **Booking Modification**: Passengers can modify certain aspects of their booking, such as travel class or food options.

5. **Food Ordering**: During the booking process, passengers can order food items from a predefined menu.

### Design Choices

1. **Data Storage**: Instead of using a database, we chose to use in-memory data structures (lists and dictionaries) to store information. This decision was made to keep the project simple and focused on the core reservation logic.

2. **Class-based Design**: We used a class-based approach for representing passengers. This allows for easy encapsulation of passenger data and methods, making the code more organized and maintainable.

3. **Distance Calculation**: We implemented a simple distance calculation method using the Pythagorean theorem. While not geographically accurate, it serves the purpose of demonstrating distance-based pricing in the system.

4. **Password Generation**: For simplicity, we generate a random 6-character alphanumeric password for each booking. In a real-world scenario, this would be replaced with a more secure user-defined password system.

### Challenges Faced

One of the main challenges was designing a system that balances simplicity for demonstration purposes with enough complexity to simulate real-world scenarios. We had to make decisions on which features to include and which to omit to keep the project manageable while still being comprehensive.

Another challenge was implementing proper error handling and input validation to ensure the system remains stable even with unexpected user inputs.

### Future Improvements

1. Implement a database system for persistent data storage.
2. Add more advanced features like seat selection and multi-city bookings.
3. Improve the distance calculation method for more accurate pricing.
4. Implement a more robust authentication system.
5. Create a graphical user interface for better user experience.

This project serves as a demonstration of object-oriented programming concepts in Python, as well as basic principles of system design and user interaction in a command-line application.
