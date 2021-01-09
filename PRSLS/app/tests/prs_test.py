import unittest

from app.models.player import Player
from app.models.prs import Prs


class PrsTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_play_game_to_tie(self):
        self.player_1 = Player("Douglas", "Rock")
        self.player_2 = Player("Marko", "Rock")
        self.assertEqual("Both Douglas and Marko have chosen Rock. That means that it's a tie!", Prs.play_game(self, self.player_1, self.player_2))

    def test_play_game_to_victory_player_1(self):
        self.player_1 = Player("Sally", "Paper")
        self.player_2 = Player("John", "Rock")
        self.assertEqual("Sally chose Paper. John chose Rock. Paper wraps Rock. Sally wins!", Prs.play_game(self, self.player_1, self.player_2))

    def test_play_game_to_victory_player_2(self):
        self.player_1 = Player("Cain", "Scissors")
        self.player_2 = Player("Abel", "Rock")
        self.assertEqual("Cain chose Scissors. Abel chose Rock. Rock crushes Scissors. Abel wins!", Prs.play_game(self, self.player_1, self.player_2))

    def test_game_must_have_valid_choice__player_1_invalid(self):
        self.player_1 = Player("Larry", "Hammer")
        self.player_2 = Player("Paula", "Paper")
        self.assertEqual("Larry must pick from the permitted choices!", Prs.play_game(self, self.player_1, self.player_2))
    
    def test_game_must_have_valid_choice__player_2_invalid(self):
        self.player_1 = Player("Larry", "Paper")
        self.player_2 = Player("Paula", "Hammer")
        self.assertEqual("Paula must pick from the permitted choices!", Prs.play_game(self, self.player_1, self.player_2))
    
    def test_game_must_have_valid_choice__both_players_invalid(self):
        self.player_1 = Player("Larry", "Hammer")
        self.player_2 = Player("Paula", "Knife")
        self.assertEqual("Both Larry and Paula must pick from the permitted choices!", Prs.play_game(self, self.player_1, self.player_2))
    


    