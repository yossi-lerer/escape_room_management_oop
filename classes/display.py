
class Display:
    @staticmethod
    def show_start_system_msg():
        print('''
    ***Escape Room Management System***
    1. For room management
    2. For reservation management
    3. for exit
    ''')

    @staticmethod    
    def show_order_management_menu():
        print('''
    1. Creating a new order.
    2. Viewing all orders.
    3. Searching for an order by ID.
    4. Viewing orders for a specific customer.
    5. Viewing orders by date.
    6. Modifying the details of an existing order.
    7. Canceling an order.
    0. for main menu
    ''')
    
    @staticmethod
    def display_escape_rooms_menu():
        print('''
    1. View all rooms.
    2. View full details of a specific room.
    3. Add a new room.
    4. Update details of an existing room.
    5. Enable or disable a room.
    0. for main menu
    ''')
        
# class Room:
#     def __init__(self, room_id, name, difficulty, duration, min_players, max_players, price_per_player, is_active=True):
#         self.room_id = room_id
#         self.is_active = is_active
#         self.update_details(name, difficulty, duration, min_players, max_players,price_per_player)

#     def update_details(self, name, difficulty, duration, min_players, max_players, price_per_player):
#         name = name.strip()
#         difficulty = difficulty.strip().capitalize()
#         if not name:
#             raise ValueError("Room name cannot be empty.")
#         if difficulty not in ("Easy", "Medium", "Hard"):
#             raise ValueError("Difficulty must be Easy, Medium or Hard.")
#         if type(duration) is not int or duration <= 0:
#             raise ValueError("Duration must be a positive number of minutes.")
#         if type(min_players) is not int or type(max_players) is not int:
#             raise ValueError("Player limits must be whole numbers.")
#         if min_players < 1 or max_players < min_players:
#             raise ValueError("Player limits must satisfy 1 <= minimum <= maximum.")
#         if not isfinite(price_per_player) or price_per_player <= 0:
#             raise ValueError("Price per player must be positive.")

#         self.name = name
#         self.difficulty = difficulty
#         self.duration = duration
#         self.min_players = min_players
#         self.max_players = max_players
#         self.price_per_player = price_per_player

# אתה בעצם יכול לשלוח בקונסטרקטור לפני יצרית הinstance ולידציות שלא קשורות לקלט אלא ללוגיקה של הROOM
    