from classes.validation import Validation

class UserInput:
    @staticmethod    
    def num_input(msg):
        user_num_input = ""
        while not Validation.validation_positive_num(user_num_input):
            user_num_input = input(msg)
        return int(user_num_input)

    @staticmethod
    def str_input(msg):
        user_text_input = ""
        while not Validation.validation_text(user_text_input):
            user_text_input = input(msg)
        return user_text_input