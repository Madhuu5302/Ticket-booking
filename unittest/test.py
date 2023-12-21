import unittest

from tic_booking.dao.ServiceRepository import TicketBookingSystem


class TestTic(unittest.TestCase):
    def test_event_creation(self):
        result = TicketBookingSystem().create_event(event_name='Tennis League', date='2023-12-31', time='18:00:00',
                                                    venue_id=1, total_seats=10,
                                                    available_seats=10, ticket_price=1, event_type='Concert')
        self.assertEqual(result, True, 'Event Creation is performed Successfully')


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
