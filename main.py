from classes.user_input import UserInput
from classes.booking_manager import BookingManager
from classes.booking import Booking
from classes.data_manager import DataManager
from classes.pricing_manager import PricingManager
from classes.room_manager import Room_management
from classes.display import Display
from classes.navigation import Navigation

class EscapeRoomSystem:
    @staticmethod
    def __init__() -> None:
        rooms = DataManager().load_rooms()
        bookings = DataManager().load_bookings()
    data_manager = DataManager
    booking_manager = BookingManager
    report_manager = PricingManager
    rooms = DataManager().load_rooms()
    bookings = DataManager().load_bookings()
    room_manager = Room_management
    display = Display
    navigation = Navigation

    def save_data(self):
        pass

    def run(self):
        while True:
            EscapeRoomSystem.display.show_start_system_msg()
            user_choose = UserInput.num_input("please enter your choose ")
            if  user_choose == 1:
                EscapeRoomSystem.navigation.manage_room_navigation()
            elif user_choose == 2:
                pass
            elif user_choose == 3:
                break

EscapeRoomSystem().run()