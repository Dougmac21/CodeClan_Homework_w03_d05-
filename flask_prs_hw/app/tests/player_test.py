import unittest

from app.models.player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player("Doug", "Rock")

    
    def test_player_has_name(self):
        self.assertEqual("Doug", self.player.name)

    def test_player_has_game_choice(self):
        self.assertEqual("Rock", self.player.game_choice)
