import unittest

from app.models.player import Player
from app.models.prs import Prs


class PrsTest(unittest.TestCase):

    def setUp(self):
        self.prs = Prs("Rock", "Paper")

    
    def test_choices_are_passed_to_game(self):
        self.assertEqual("Rock", self.prs.player_1_choice)
        self.assertEqual("Paper", self.prs.player_2_choice)
        



    


    