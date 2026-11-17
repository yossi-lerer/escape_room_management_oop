class ReportManager:
    def __init__(self, rooms, bookings ) -> None:
        self.rooms = rooms
        self.bookings = bookings

    def count_active_bookings(self):
        pass

    def count_cancelled_bookings(self):
        pass

    def calculate_total_revenue(self):
        pass

    def calculate_cancellation_revenue(self):
        pass

    def get_most_popular_room(self):
        pass

    def get_room_booking_count(self, room_id):
        pass

    def calculate_occupancy(self, room_id, booking_date):
        pass