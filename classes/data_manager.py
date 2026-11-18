import json
from pathlib import Path
from classes.room import Room
from classes.booking import Booking


class DataManager():
    def __new__(cls):
        if not hasattr(cls, 'inst'):
            cls.inst = super().__new__(cls)
        return cls.inst
    
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
            list_of_rooms = []
            for room in rooms:
                list_of_rooms.append(room.to_dict())
            records = json.dumps(list_of_rooms, indent=4)
            file.write(records)

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
