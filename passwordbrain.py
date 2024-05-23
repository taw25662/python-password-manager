import random
import string
import random


# This class will generate passwords
class Pb:
    def __init__(self):
        self.characters = list(string.ascii_letters + string.digits)
        self.new_password_list = []

    # Create a strong 12-character password with the random module
    def generate_password(self):
        self.clear_memory()
        for x in range(0,12):
            character = random.choice(self.characters)
            self.new_password_list.append(character)
            # Create a password with a hyphen every 4 characters
            password = '-'.join([''.join(self.new_password_list[i:i+4]) for i in range(0, len(self.new_password_list), 4)])
        return password

    # Clear the self.list to create a new password
    def clear_memory(self):
        self.new_password_list = []





