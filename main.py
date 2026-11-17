from classes.user_input import UserInput
from classes.booking_manager import BookingManager
from classes.booking import Booking
from classes.data_manager import DataManager
from classes.pricing_manager import PricingManager
import os
class EscapeRoomSystem:
    def __init__(self) -> None:
        self.data_manager = DataManager
        self.booking_manager = BookingManager
        self.report_manager = PricingManager
        self.rooms = DataManager().load_rooms()
        self.bookings = DataManager().load_bookings()

    def display_menu(self):
        print('''
    1. View all rooms.
    2. View full details of a specific room.
    3. Add a new room.
    4. Update details of an existing room.
    5. Enable or disable a room.
    0. for main menu
    ''')
        for booking in self.bookings:
            print("\nBooking Details:")
            for key, value in booking.to_dict().items():
                print(f"{key}: {value}")
                
    def save_data(self):
        pass

    def run(self):
        self.display_menu()
        UserInput.str_input("please enter your choose ")

EscapeRoomSystem().run()