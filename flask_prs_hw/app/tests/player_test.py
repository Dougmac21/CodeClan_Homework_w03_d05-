import unittest

from app.models.player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player("Doug", "Rock")

    
    def test_player_has_name(self):
        self.assertEqual("Doug", self.player.name)

    def test_player_has_game_choice(self):
        self.assertEqual("Rock", self.player.game_choice)

    def test_can_have_two_players(self):
        self.player_1 = Player("Marko", "Scissors")
        self.player_2 = Player("Polo", "Paper")
        self.assertEqual("Marko", self.player_1.name)
        self.assertEqual("Polo", self.player_2.name)
        self.assertEqual("Scissors", self.player_1.game_choice)
        self.assertEqual("Paper", self.player_2.game_choice)

    def test_game_choices_are_limited(self):
        self.player_1 = Player("Marko", "Scissors")
        self.player_2 = Player("Polo", "Hammer")
        self.assertEqual("Scissors", self.player_1.game_choice)
        self.assertEqual("You must choose paper, rock or scissors.", self.player_2.game_choice)