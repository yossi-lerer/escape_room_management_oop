from classes.user_input import UserInput
from classes.display import Display
from classes.room_manager import Room_management

class Navigation:
    @staticmethod
    def manage_room_navigation():
        while True:
            Display.display_escape_rooms_menu()
            user_select = UserInput.num_input("Select a number from the menu: ")
            if user_select == 1:
                Room_management.view_all_rooms()
            if user_select == 2:
                room_id = UserInput.num_input("(int) enter room id: ")
                Room_management.view_room_by_id(room_id)
            if user_select == 3:
                room_name = UserInput.str_input("(str) enter room name: ")
                difficulty = UserInput.str_input("(str) enter difficulty: ")
                duration = UserInput.num_input("(int) enter duration: ")
                min_players = UserInput.num_input("(int) enter min players: ")
                max_players = UserInput.num_input("(int) enter max players: ")
                price_per_player = UserInput.num_input("(int) price per player: ")
                Room_management.Add_a_new_room(room_name, difficulty, duration, min_players, max_players, price_per_player)
            if user_select == 4:
                room_id = UserInput.num_input("(int) enter room id: ")
                key = UserInput.str_input("(str) enter key to update: ")
                value = UserInput.str_input("(str) enter value to update: ")
                print(Room_management.update_room(room_id, key, value))
            if user_select == 5:
                room_id = UserInput.num_input("(int) enter room id: ")
                Room_management.enable_or_disable_room(room_id)
            if user_select == 0:
                break
    
    # @staticmethod
    # def manage_order_navigation():
    #     while True:
    #         Display.show_order_management_menu()
    #         user_select = UserInput.num_input("Select a number from the menu: ")
    #         if user_select == 1:
    #             data = main_validate_booking(30)
    #             creating_a_new_order(data)
    #         if user_select == 2:
    #             view_all_orders()
    #         if user_select == 3:
    #             booking_id = "B001"
    #             view_order_by_id(booking_id)
    #         if user_select == 4:
    #             customer_name = "Moshe Israel"
    #             view_orders_by_customer(customer_name)
    #         if user_select == 5:
    #             booking_date = "2026-11-14"
    #             view_orders_by_date(booking_date)
    #         if user_select == 6:
    #             edit_existing_order("B001", "players", 5)
    #         if user_select == 7:
    #             cancel_an_order("B001")
    #         if user_select == 0:
    #             break