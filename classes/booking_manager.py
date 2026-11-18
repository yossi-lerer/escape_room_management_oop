from classes.data_manager import DataManager
from classes.pricing_manager import PricingManager
from classes.booking import Booking

class BookingManager:
    rooms = DataManager().load_rooms()
    bookings =  DataManager().load_bookings()
    pricing_manager = PricingManager()

    def create_booking(self, customer_name, room_id, booking_date, start_time, players):
        record =     {
        "booking_id": 5,
        "customer_name": "David Cohen",
        "room_id": "R001",
        "booking_date": "2026-11-14",
        "start_time": "10:00",
        "players": 5,
        "total_price": 320.0,
        "status": "Cancelled",
        "cancellation_fee": 0.0
    }

    def get_booking(self, booking_id):
        pass

    def get_customer_bookings(self, customer_name):
        pass

    def get_bookings_by_date(self, booking_date):
        pass

    def check_availability(self, room_id, booking_date, start_time, exclude_booking_id=None):
        pass

    def update_booking(self, booking_id, booking_date, start_time, players):
        pass

    def cancel_booking(self, booking_id, current_datetime):
        pass