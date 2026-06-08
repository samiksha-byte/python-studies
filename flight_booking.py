flights = {
    "AI101": {"source": "Delhi", "dest": "Mumbai", "seats": 5, "price": 5500},
    "AI102": {"source": "Mumbai", "dest": "Delhi", "seats": 8, "price": 5200},
    "6E201": {"source": "Bangalore", "dest": "Chennai", "seats": 3, "price": 3200},
    "6E202": {"source": "Chennai", "dest": "Bangalore", "seats": 4, "price": 3100},
    "UK301": {"source": "Delhi", "dest": "Kolkata", "seats": 2, "price": 6000},
    "UK302": {"source": "Kolkata", "dest": "Delhi", "seats": 6, "price": 6200},
    "SG401": {"source": "Hyderabad", "dest": "Pune", "seats": 10, "price": 4000},
    "SG402": {"source": "Pune", "dest": "Hyderabad", "seats": 7, "price": 4100},
    "QP501": {"source": "Ahmedabad", "dest": "Delhi", "seats": 5, "price": 3500},
    "QP502": {"source": "Delhi", "dest": "Ahmedabad", "seats": 9, "price": 3600}
}


def search_flight(source, destination):
    for flight_no, details in flights.items():
        if details["source"].lower() == source.lower() and details["dest"].lower() == destination.lower():
            return flight_no, details
    return None, None


def book_ticket():
    source = input("Enter Source Airport: ")
    destination = input("Enter Destination Airport: ")

    flight_no, details = search_flight(source, destination)

    if flight_no is None:
        print("No flights available")
        return

    print("\nFlight Found")
    print("Flight Number:", flight_no)
    print("Source:", details["source"])
    print("Destination:", details["dest"])
    print("Available Seats:", details["seats"])
    print("Ticket Price:", details["price"])

    seats_required = int(input("\nEnter number of seats required: "))

    if seats_required <= details["seats"]:
        details["seats"] = details["seats"] - seats_required

        total_amount = seats_required * details["price"]

        print("\nBooking Confirmed")
        print("Flight Number:", flight_no)
        print("Seats Booked:", seats_required)
        print("Total Amount:", total_amount)
        print("Remaining Seats:", details["seats"])

    else:
        print("Requested seats not available")


book_ticket()
