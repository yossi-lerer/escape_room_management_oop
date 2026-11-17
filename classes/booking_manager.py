class BookingManager:
    def __init__(self, rooms, bookings, pricing_manager) -> None:
        self.rooms = rooms
        self.bookings = bookings
        self.pricing_manager = pricing_manager

    def create_booking(self, customer_name, room_id, booking_date, start_time, players):
        pass

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