# task 1.1 , 1.2
def book_tickets(available_tickets, booking_tickets):
    if available_tickets < booking_tickets:
        print("Not enough tickets available.")
    else:
        remaining_tickets = available_tickets - booking_tickets
        print(f"Booking successful! {booking_tickets} tickets booked. {remaining_tickets} tickets remaining.")


try:
    available_ticket = int(input("Enter the number of available tickets: "))
    no_of_booking_ticket = int(input("Enter the number of tickets you want to book: "))
    book_tickets(available_ticket, no_of_booking_ticket)
except ValueError:
    print("Please enter valid numerical values.")

    # task 2,3


def ticket_cost(ticket_category, num_tickets):
    base_prices = {"Silver": 50, "Gold": 100, "Diamond": 150}

    try:
        base_price = base_prices[ticket_category]
        total_cost = base_price * num_tickets
        print(f"Total cost for {num_tickets} {ticket_category} tickets: Rs.{total_cost}")
    except KeyError:
        print("Invalid ticket category. Please choose Silver, Gold, or Diamond.")


while True:
    try:
        print("Ticket Options:")
        print("1. Silver - Rs.50")
        print("2. Gold - Rs.100")
        print("3. Diamond - Rs.150")
        print("Type Exit to close")
        ticket_category = input("Enter the ticket category (Silver/Gold/Diamond): ")

        if ticket_category == "Exit":
            break
        num_tickets = int(input("Enter the number of tickets you want to book: "))
        ticket_cost(ticket_category, num_tickets)
    except ValueError:
        print("Please enter valid numerical values.")
