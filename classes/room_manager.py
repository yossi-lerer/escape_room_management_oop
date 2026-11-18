from classes.data_manager import DataManager
from classes.pricing_manager import PricingManager
from classes.booking import Booking
from classes.room import Room

class Room_management:
    rooms = DataManager().load_rooms()
    
    @staticmethod
    def view_all_rooms():
        for record in Room_management.rooms:
            for key in record.to_dict():
                print(f"{key}: {record.to_dict()[key]}")
            print("\n==============================================")

    @staticmethod
    def view_room_by_id( room_id):
        room_id = f"R{room_id + 1:03d}"
        for record in Room_management.rooms:
            if record.to_dict()["room_id"] == room_id:
                for key in record.to_dict():
                    print(f"{key}: {record.to_dict()[key]}")
                print("\n==============================================")


    @staticmethod
    def Add_a_new_room(name, difficulty, duration, min_players, max_players, price_per_player):
        record = {
            "room_id": f"R{len(Room_management.rooms) + 1:03d}",
            "name": name,
            "difficulty": difficulty,
            "duration": duration,
            "min_players": min_players,
            "max_players": max_players,
            "price_per_player": price_per_player,
            "is_active": True
        }
        new_record = Room.from_dict(record)
        rooms = Room_management.rooms
        rooms.append(new_record)
        DataManager.save_rooms(rooms)
        return

    @staticmethod
    def update_room(room_id, key, value):
        room_id = f"R{room_id:03d}"
        try:
            for record in Room_management.rooms:
                record = record.to_dict()
                if record["room_id"] == room_id:
                    record[key]
                    record[key] = value
                    DataManager.save_rooms(Room_management.rooms)
                    return record
            
        except:
            return "key not found"
    
    @staticmethod
    def enable_or_disable_room(room_id):
        room_id = f"R{room_id:03d}"
        for record in Room_management.rooms:
            record = record.to_dict()
            
            if record["room_id"] == room_id:
                if record["is_active"] == True:
                    record["is_active"] = False
                else:
                    record["is_active"] = True
        DataManager.save_rooms(Room_management.rooms)
