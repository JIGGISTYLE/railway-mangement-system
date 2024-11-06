
from passenger import Passenger
from data import passenger_list, food_menu, class_details

def display_menu():
    message = """
---------------------------------------------------------------------------------------------------------------------

                        🚂🌟 **WELCOME TO OUR RAILWAY RESERVATION SYSTEM** 🌟🚂

                        1. Reserve a Ticket 🎫
                        2. Check PNR Status 📊
                        3. Cancel a Ticket ❌
                        4. Modify Booking 🔄
                        5. Quit 🚪

                        Your journey begins here! 🌠

---------------------------------------------------------------------------------------------------------------------
    """
    print(message)

def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice: ").strip())
            if 1 <= choice <= 5:
                return choice
            else:
                print("\nInvalid choice. Please select a valid option.")
        except ValueError:
            print("\nPlease enter a valid number.")

def book_ticket():
    total_amount = 0
    while True:
        try:
            name = input("Enter passenger's name: ").strip()
            age = int(input("Enter passenger's age: ").strip())
            gender = input("Enter passenger's gender (male/female/other): ").strip().lower()
            phone_no = input("Enter mobile number: ").strip()
            train_no = int(input("Enter train number: ").strip())
            from_station = input("Enter departure station: ").strip().lower()
            to_station = input("Enter arival station: ").strip().lower()

            print("Select a class you would like to travel in:")
            for class_no, class_name in class_details.items():
                print(f"{class_no}. {class_name}")

            travel_class = int(input("Enter your choice: ").strip())

            food_items = select_food_items()

            passenger = Passenger(name, age, gender, phone_no, train_no, travel_class, from_station, to_station, food_items)
            passenger_list.append(passenger)
            total_amount += passenger.amount
            print(f"\n{name} has been successfully added with PNR {passenger.pnr} and password {passenger.password}. Your seat number is {passenger.seat_number} in coach {passenger.coach}. Please keep your PNR and password confidential to prevent misuse.")


        except ValueError as e:
            print(f"\nError: {e}")

        ch = input("\nDo you want to add another passenger? (yes/no): ").strip().lower()
        if ch != "yes":
            break

    print(f"\nTotal amount to be paid: ₹{total_amount:.2f}")
    print("\nInsertion completed")

def select_food_items():
    food_items = []
    want_food = input("Do you want to order food? (yes/no): ").strip().lower()
    if want_food == 'yes':
        while True:
            print("Please choose your food items (type 'done' when finished):")
            for idx, (food_item, cost) in enumerate(food_menu.items(), 1):
                print(f"{idx}. {food_item} - {cost}")
            food_choice = input("Enter your choice: ").strip().lower()
            if food_choice == 'done':
                break
            try:
                food_idx = int(food_choice) - 1
                if 0 <= food_idx < len(food_menu):
                    food_items.append(list(food_menu.keys())[food_idx])
                else:
                    print("\nInvalid choice. Please try again.")
            except ValueError:
                print("\nInvalid input. Please enter a number or 'done'.")
    return food_items

def display_pnr_status():
    try:
        pnr = int(input("Enter PNR number: "))
        for _ in range(3):
            password = input("Enter password: ").strip()
            for passenger in passenger_list:
                if passenger.pnr == pnr and passenger.password == password:
                    print(f"\n\nPassenger details are: {passenger.get_details()}")
                    return
            print("\nIncorrect password. Try again.")
        print("\nPNR or password not found after 3 attempts.")
    except ValueError:
        print("\nInvalid PNR number.")

def cancel_ticket():
    try:
        pnr = int(input("Enter PNR number: "))
        for _ in range(3):
            password = input("Enter password: ").strip()
            for passenger in passenger_list:
                if passenger.pnr == pnr and passenger.password == password:
                    warning=f"""
############################################################################################################################################################
                                             ⚠️ **Important Notice: Train Ticket Cancellation**



Dear {passenger.name},

We regret to inform you that in case of ticket cancellation, a deduction of 18% will be applicable as Goods and Services Tax (GST).
This deduction will be calculated on the total fare of your ticket.

Please proceed with caution and consider this while cancelling your reservation. For any further assistance, feel free to contact our customer support.


                                                        Safe travels!


###########################################################################################################################################################
"""
                    print(warning)
                    confirm = input("Do you want to proceed with the cancellation? (yes/no): ").strip().lower()
                    if confirm == 'yes':
                        refund_amount = passenger.amount * 0.82  # Apply 18% deduction
                        print(f"Ticket cancelled. Refund amount: ₹{refund_amount:.2f} will be credited to your registered bank account on your registered mobile number within 2-3 working days.")
                        passenger_list.remove(passenger)
                    else:
                        print("\nCancellation aborted.")
                    return
            print("\nIncorrect password. Try again.")
        print("\nPNR or password not found after 3 attempts.")
    except ValueError:
        print("\nInvalid PNR number.")

def modify_booking():
    try:
        pnr = int(input("Enter PNR number: "))
        for _ in range(3):
            password = input("Enter password: ").strip()
            for passenger in passenger_list:
                if passenger.pnr == pnr and passenger.password == password:
                    print("Passenger found. What would you like to modify?")
                    print("1. Travel Class")
                    print("2. Food Items")
                    print("3. Contact Information")
                    choice = int(input("Enter your choice: ").strip())

                    if choice == 1:
                        print("Select a new class you would like to travel in:")
                        for class_no, class_name in class_details.items():
                            print(f"{class_no}. {class_name}")
                        new_travel_class = int(input("Enter your choice: ").strip())
                        passenger.travel_class = passenger.validate_travel_class(new_travel_class)
                        passenger.amount = passenger.calculate_ticket_cost() + sum(food_menu[item] for item in passenger.food_items)
                        print(f"Travel class updated to {class_details[new_travel_class]}. New amount: {passenger.amount:.2f}")

                    elif choice == 2:
                        new_food_items = select_food_items()
                        passenger.food_items = new_food_items
                        passenger.amount = passenger.calculate_ticket_cost() + sum(food_menu[item] for item in new_food_items)
                        print(f"Food items updated. New amount: {passenger.amount:.2f}")

                    elif choice == 3:
                        new_phone_no = input("Enter new mobile number: ").strip()
                        passenger.phone_no = passenger.validate_phone_no(new_phone_no)
                        print(f"Contact information updated to {new_phone_no}")

                    else:
                        print("Invalid choice.")
                    return
            print("Incorrect password. Try again.")
        print("PNR or password not found after 3 attempts.")
    except ValueError:
        print("Invalid input.")

def main():
    while True:
        display_menu()
        choice = get_choice()
        if choice == 1:
            book_ticket()
        elif choice == 2:
            display_pnr_status()
        elif choice == 3:
            cancel_ticket()
        elif choice == 4:
            modify_booking()
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
