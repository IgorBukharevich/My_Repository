"""
Task 3: Make email filtering function
"""
import re


class ValidateEmail:
    """class ValidateEmail"""

    def __init__(self, email):
        self.email = email

    def check_email(self):
        """email validity check"""
        pattern = "^([^.])([a-z.-]+)@([a-z]{2,63})+.([a-z]{2,3})$"

        if re.match(pattern, self.email):
            print("Validly!")
        else:
            print('Not valid')


user_email = ValidateEmail('igor.bukharevich.lifanor@gmail.com')
user_email.check_email()
