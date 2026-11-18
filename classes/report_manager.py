from classes.data_manager import DataManager

class ReportManager:
    rooms = DataManager.load_rooms()
    bookings = DataManager.load_bookings()

    @staticmethod
    def count_active_bookings():
        total = 0
        for booking in ReportManager.bookings:
            booking = booking.to_dict()
            if booking["status"] == "Active":
                total += 1
        return total
    
    @staticmethod
    def count_cancelled_bookings():
        total = 0
        for booking in ReportManager.bookings:
            booking = booking.to_dict()
            if booking["status"] == "Cancelled":
                total += 1
        return total

    @staticmethod
    def calculate_total_revenue():
        total = 0
        for booking in ReportManager.bookings:
            booking = booking.to_dict()
            if booking["status"] == "Active":
                total += booking["total_price"]
        return total

    @staticmethod
    def calculate_cancellation_revenue():
        total = 0
        for booking in ReportManager.bookings:
            booking = booking.to_dict()
            if booking["status"] == "Cancelled":
                total += booking["cancellation_fee"]
        return total

    @staticmethod
    def get_most_popular_room():
        rooms_calculate = {}
        for booking in ReportManager.bookings:
            booking = booking.to_dict()
            if booking["room_id"] in rooms_calculate:
                rooms_calculate[booking["room_id"]] += 1
            else:
                rooms_calculate[booking["room_id"]] = 1
        sort = sorted(rooms_calculate.items(), key=lambda item: item[1], reverse=True)
        return sort[0][0]

    @staticmethod
    def get_room_booking_count(room_id):
        total = 0
        for booking in ReportManager.bookings:
            booking = booking.to_dict()
            if booking["room_id"] == room_id:
                total += 1
        return total
    
    @staticmethod
    def calculate_occupancy(room_id, booking_date):
        total = 0
        duration = 0
        for room in ReportManager.rooms:
            room = room.to_dict()
            if room["room_id"] == room_id:
                duration = room["duration"] + 15
                break
    
        for booking in ReportManager.bookings:
            booking = booking.to_dict()
            if booking["room_id"] == room_id or booking["booking_date"] == booking_date:
                total += duration
        return total / 720 * 100