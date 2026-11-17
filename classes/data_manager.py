import json
from pathlib import Path
from classes.room import Room
from classes.booking import Booking


class DataManager():
    rooms_file = "./db/rooms.json"
    bookings_file = "./db/bookings.json"

    @staticmethod
    def load_rooms():
        if not Path(DataManager.rooms_file).exists():
            return []
        with open(DataManager.rooms_file, "r") as file:
            rooms_data = json.load(file)
            return [Room.from_dict(room) for room in rooms_data]
    
    @staticmethod
    def save_rooms(rooms):
        with open(DataManager.rooms_file, "w") as file:
            json.dump([room.to_dict() for room in rooms], file, indent=4)

    @staticmethod
    def load_bookings():
        if not Path(DataManager.bookings_file).exists():
            return []
        with open(DataManager.bookings_file, "r") as file:
            bookings_data = json.load(file)
            return [Booking.from_dict(booking) for booking in bookings_data]
    
    @staticmethod
    def save_bookings(bookings):
        with open(DataManager.bookings_file, "w") as file:
            json.dump([booking.to_dict() for booking in bookings], file, indent=4)  
