"""
Task 1: Create a @dataclass
Task 2: Add a @staticmethod to the class
Task 3: add to the @classmethod
"""
from dataclasses import dataclass
import time


@dataclass
class GameInfo:
    """creating dataclass"""
    title: str
    developer: str
    publisher: str
    localizer: str
    release_date: int
    latest_version: str
    composer: str


class SomeClass:
    """Game data initialization class"""
    load_text = "Uploading game data"  # attributes class SomeClass

    def __init__(self, book):
        # initializing attributes
        self.book = book

    def show_data(self):
        """data output method"""

        print(
            f'-------------------------------------\n'
            f'Title: {self.book.title}\n'
            f'Developer: {self.book.developer}\n'
            f'Publisher: {self.book.publisher}\n'
            f'Localizer: {self.book.localizer}\n'
            f'Release date: {self.book.release_date}\n'
            f'Latest version: {self.book.latest_version}\n'
            f'Composer: {self.book.composer}\n'
            f'-------------------------------------\n'
        )

    @staticmethod
    def simulate_load():
        """simulated loading"""

        print('Loading...')
        time.sleep(2)

    @classmethod
    def show_massage(cls):
        """message output"""
        print(cls.load_text)


# information about the game World of Warcraft
wow_lich_king = GameInfo(
    title='World of Warcraft: Wrath of the Lich King',
    developer='Blizzard Entertainment',
    publisher='Blizzard Entertainment',
    localizer='Blizzard Entertainment',
    release_date=2008,
    latest_version='3.3.5a',
    composer='Russell Brower'
)

# information about the game CS:GO
cs_go = GameInfo(
    title='Counter-Strike: Global Offensive',
    developer='Valve',
    publisher='Valve',
    localizer='Buka Entertainment Enterprises',
    release_date=2012,
    latest_version='1.38.4.3',
    composer='Mike Morasky'
)

SomeClass.show_massage()
SomeClass.simulate_load()

wow_game = SomeClass(wow_lich_king)
wow_game.show_data()

cs_go_game = SomeClass(cs_go)
cs_go_game.show_data()
