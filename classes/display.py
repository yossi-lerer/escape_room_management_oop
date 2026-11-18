
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