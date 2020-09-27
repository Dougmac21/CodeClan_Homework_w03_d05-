import unittest

from app.models.player import Player
from app.models.prs import Prs


class PrsTest(unittest.TestCase):

    def setUp(self):
        self.prs = Prs.play_game(self, "Rock", "Paper")


    def test_play_game_to_tie(self):
        self.player_1 = Player("Douglas", "Rock")
        self.player_2 = Player("Marko", "Rock")
        self.assertEqual("It's a tie!", Prs.play_game(self, self.player_1.game_choice, self.player_2.game_choice))

    def test_play_game_to_victory(self):
        self.player_1 = Player("Sally", "Paper")
        self.player_2 = Player("John", "Rock")
        self.assertEqual("Somebody has won!", Prs.play_game(self, self.player_1.game_choice, self.player_2.game_choice))




    


    