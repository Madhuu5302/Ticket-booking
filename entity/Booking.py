from datetime import timedelta
from tic_booking.entity.Event import Event
from tic_booking.util.DBConnUtil import DbConn

class Booking(DbConn):
    def __init__(self, customer_id, event_id, num_tickets):
        self.customer_id = customer_id
        self.event_id = event_id
        self.num_tickets = num_tickets

    def calculate_booking_cost(self):
        try:
            event = self.get_event()
            return self.num_tickets * event.get_ticket_price()
        except Exception as e:
            print(e)

    def book_tickets(self):
        try:
            event = self.get_event()

            if event.book_tickets(self.num_tickets):
                total_cost = self.num_tickets * event.get_ticket_price()
                booking_date = event.get_event_date() - timedelta(days=4)

                self.open()
                self.stmt.execute(
                    f"INSERT INTO Booking (customer_id, event_id, num_tickets, "
                    f"total_cost, booking_date) VALUES ({self.customer_id}, {self.event_id}, {self.num_tickets}, {total_cost}, '{booking_date}')")
                self.conn.commit()
                booking_id = self.stmt.lastrowid
                self.close()

                print(f"\nBooking Done Successfully...\nYour Booking ID is : {booking_id}\nAmount to be Paid : {total_cost}")
                return booking_id
        except Exception as e:
            print(e)

    def cancel_booking(self):
        try:
            event = self.get_event()
            total_cost = self.num_tickets * event.get_ticket_price()

            self.open()
            self.stmt.execute(f"DELETE FROM Booking WHERE booking_id = {self.booking_id}")
            self.conn.commit()
            self.close()

            event.cancel_booking(self.num_tickets)

            print(f"\nCancellation successful... \nRefund amount: {total_cost}")
            return self.booking_id
        except Exception as e:
            print(e)

    def get_available_no_of_tickets(self):
        try:
            event = self.get_event()
            return event.available_seats
        except Exception as e:
            print(e)

    def get_event(self):
        try:
            self.open()
            self.stmt.execute(f"SELECT * FROM Event WHERE event_id = {self.event_id}")
            event_data = self.stmt.fetchone()
            self.close()
            return Event(*event_data)
        except Exception as e:
            print(e)

    def get_event_details(self):
        try:
            event = self.get_event()
            event.display_event_details()
        except Exception as e:
            print(e)
