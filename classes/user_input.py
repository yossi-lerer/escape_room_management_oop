class UserInput:

    @staticmethod
    def num_input(msg):
        user_num_input = input(msg)
        return int(user_num_input)

    @staticmethod
    def str_input(msg):
        user_text_input = input(msg)
        return user_text_input