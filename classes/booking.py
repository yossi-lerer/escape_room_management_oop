class Booking:
    def __init__(self, booking_id, customer_name, room_id, booking_date, start_time, players, total_price, status, cancellation_fee) -> None:
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.room_id = room_id
        self.booking_date = booking_date
        self.start_time = start_time
        self.players = players
        self.total_price = total_price
        self.status = status
        self.cancellation_fee = cancellation_fee

    def cancel(self):
        pass

    def update_details(self, booking_date, start_time, players, total_price):
        pass

    def to_dict(self):
        pass

    def from_dict(self):
        pass