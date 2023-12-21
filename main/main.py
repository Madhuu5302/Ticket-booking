import mysql.connector as connection
from tic_booking.util.DBConnUtil import DbConn
from tic_booking.entity.Event import Event
from tic_booking.dao.ServiceRepository import TicketBookingSystem
from tic_booking.exceptions.myexceptions import EventNotFoundException, InvalidBookingIDException


class EventBookingApp(DbConn):
    def __init__(self):
        super().__init__()
        self.ticket_system = TicketBookingSystem()
        self.menu_options = {
            1: self.host_new_event,
            2: self.book_tickets_for_event,
            3: self.view_existing_booking,
            4: self.cancel_booking,
            5: self.exit_program
        }

    def display_main_menu(self):
        print("1. Host a New Event")
        print("2. Book Tickets for an Event")
        print("3. View Existing Booking Details")
        print("4. Cancel a Booking")
        print("5. Exit")

    def host_new_event(self):
        print("\n-------- HOST NEW EVENT --------")
        event_name = input('Enter the Event Name: ')
        event_types_dict = {'S': 'Sports', 'C': 'Concert', 'M': 'Movie'}

        event_type_input = input("Select the Event Type (S for Sports, C for Concert, M for Movies): ").upper()
        event_type = event_types_dict.get(event_type_input)

        if not event_type:
            print('Invalid Event Type. Redirecting to Main Menu...')
            return

        date = input("Enter Date in the 'yyyy-mm-dd' format: ")
        time = input("Enter Time in the 'hh:mm:ss' format: ")

        venue = self.ticket_system.get_random_venue(event_type, date)

        if venue is None:
            print('No Venues are Available for the entered Date...')
            return

        total_seats = int(input('Enter the Total Seats for the Event: '))
        available_seats = int(input('Enter the Available Tickets for the Event: '))
        ticket_price = float(input('What should be the ticket price: '))

        self.ticket_system.create_event(event_name, date, time, venue[4], total_seats, available_seats, ticket_price,
                                        event_type)

    def book_tickets_for_event(self):
        print("\n-------- BOOK TICKETS FOR EVENT --------")
        print("1. Display a Particular Event Details")
        print("2. Display Events of a Particular Type")

        sub_choice = input("Enter your choice: ")

        if not sub_choice.isdigit():
            print("Invalid input. Please enter a number.")
            return

        sub_choice = int(sub_choice)

        if sub_choice == 1:
            event_name_input = input('Enter the Event Name: ').lower()
            event_object = self.ticket_system.get_event_by_name(event_name_input)

            if event_object is None:
                print(f"No Event Exists with the name: {event_name_input}")
                return

            self.ticket_system.display_event_details(event_object)

        elif sub_choice == 2:
            print('Select the Event Type you are looking to attend...')
            print("Press 'S' for Sports, 'C' for Concert, and 'M' for Movies")

            event_type_input = input().upper()
            event_type = {'S': 'Sports', 'C': 'Concert', 'M': 'Movie'}.get(event_type_input)

            if not event_type:
                print('\nInvalid Event Type. Redirecting to Main Menu...')
                return

            event_list = self.ticket_system.get_events_by_type(event_type)

            for event_data in event_list:
                Event(*event_data).display_event_details()
                print('\n')

            event_id_input = input('From the list above, enter the ID of Event you are interested to attend: ')

            if not event_id_input.isdigit():
                print("Invalid input. Please enter a number.")
                return

            event_id_input = int(event_id_input)
            event_object = self.ticket_system.get_event_by_id(event_id_input, event_list)

            if event_object is None:
                print('No such Event ID exists in the above list!!')
                return

        else:
            print('Invalid Choice. Redirecting to Main Menu...')
            return

        num_tickets = input('Enter the Number Of Tickets you want to Book: ')

        if not num_tickets.isdigit():
            print("Invalid input. Please enter a number.")
            return

        num_tickets = int(num_tickets)
        self.ticket_system.book_tickets(event_object, num_tickets)

    def view_existing_booking(self):
        print("\n-------- VIEW EXISTING BOOKING --------")
        booking_id_input = input("Enter Booking ID to retrieve Booking Details: ")

        if not booking_id_input.isdigit():
            print("Invalid input. Please enter a number.")
            return

        booking_id_input = int(booking_id_input)
        booking_details = self.ticket_system.get_booking_details(booking_id_input)

        if booking_details is None:
            print(f'No booking found with ID: {booking_id_input}. Redirecting to Main Menu...')
            return

        print('Customer ID: ', booking_details[1])
        print('Event ID: ', booking_details[2])
        print('Number of Tickets Booked: ', booking_details[3])
        print('Total Cost of Booking: ', booking_details[4])
        print('Booking Date: ', booking_details[5])

    def cancel_booking(self):
        print("\n-------- CANCEL BOOKING --------")
        booking_id_input = input("Enter Booking ID to be Cancelled: ")

        if not booking_id_input.isdigit():
            print("Invalid input. Please enter a number.")
            return

        booking_id_input = int(booking_id_input)

        event_object, num_tickets_for_cancel = self.ticket_system.cancel_tickets(booking_id_input)

        if event_object is None:
            print(f'No booking found with ID: {booking_id_input}. Redirecting to Main Menu...')
            return

        print('Booking has been cancelled for the Booking ID: ', booking_id_input)

    def exit_program(self):
        print('\n===================== THANK YOU =====================')
        print('Please Visit Again.....\n')
        exit()

    def main(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")

            if not choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            choice = int(choice)

            selected_option = self.menu_options.get(choice)
            if selected_option:
                selected_option()
            else:
                print('\nInvalid Choice. Please Try Again....')


if __name__ == '__main__':
    EventBookingApp().main()
