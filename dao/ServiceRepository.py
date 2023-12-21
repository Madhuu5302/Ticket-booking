import mysql.connector as connection
from tic_booking.util.DBConnUtil import DbConn
from tic_booking.entity.Booking import Booking


class TicketBookingSystem(DbConn):
    def __init__(self):
        super().__init__()

    def create_event(self, event_name, date, time, venue_id, total_seats, available_seats, ticket_price, event_type):
        try:
            self.open()
            self.stmt.execute(
                f"INSERT INTO Event (event_name, event_date, event_time, venue_id, "
                f"total_seats, available_seats, ticket_price, event_type) VALUES ('"
                f"{event_name}', '{date}', '{time}', {venue_id}, {total_seats}, "
                f"{available_seats}, {ticket_price}, '{event_type}')")
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        else:
            print('\nEvent Added Successfully')
            return True
        finally:
            self.close()

    @staticmethod
    def display_event_details(event_obj):
        event_obj.display_event_details()

    def book_tickets(self, event_obj, num_tickets):
        name = input('Enter Your Name: ')
        email = input('Enter Your Email-ID: ')
        phone_no = input('Enter Your Phone Number: ')

        try:
            self.open()
            self.stmt.execute(
                f"INSERT INTO Customer (customer_name, email, phone_number) "
                f"VALUES ('{name}', '{email}', '{phone_no}')")
            self.conn.commit()
            customer_id = self.stmt.lastrowid
        except Exception as e:
            print(e)
            return False
        finally:
            self.close()

        event_id = event_obj.get_event_id()
        Booking(customer_id=customer_id, event_id=event_id, num_tickets=num_tickets).book_tickets()

    @staticmethod
    def cancel_tickets(event_obj, num_tickets):
        event_obj.cancel_booking(num_tickets)


if __name__ == '__main__':
    # Example usage
    ticket_system = TicketBookingSystem()

    # Create an event
    ticket_system.create_event("Concert", "2023-12-25", "20:00:00", 1, 100, 100, 50.0, "Concert")

    # Assuming you have an Event object, you can display its details
    event_obj = Event(event_id=1, event_name="Concert", event_date="2023-12-25", event_time="20:00:00",
                      venue_id=1, total_seats=100, available_seats=50, ticket_price=50.0, event_type="Concert")
    ticket_system.display_event_details(event_obj)

    # Book tickets for an event
    ticket_system.book_tickets(event_obj, 2)

    # Cancel tickets for an event
    ticket_system.cancel_tickets(event_obj, 2)
