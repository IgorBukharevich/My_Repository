"""
My exception class is checking division by zero
"""


class CheckZero(Exception):
    """My exception class"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "You can't divide by zero!!!"
