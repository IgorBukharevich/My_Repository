"""
Task 1: Create a geometric progression generator
Task 2: Connect the debugger
"""


class Generator:
    """class Generator"""
    def __init__(self, start: int, ratio: int, count_elem: int):
        """initializing attributes"""
        self.start = start
        self.ratio = ratio
        self.count_elem = count_elem

    def gen_option_1(self):
        """the first generation method"""
        for n in range(1, self.count_elem + 1):
            elem = self.start * self.ratio ** (n - 1)
            yield elem

    def gen_option_2(self):
        """the second generation method"""
        geometric = [
            self.start * self.ratio ** (n - 1)
            for n in range(1, self.count_elem + 1)
        ]
        return geometric


use_1 = Generator(1, 5, 10)
# first method
print(list(use_1.gen_option_2()))
# second method
print(list(use_1.gen_option_1()))
