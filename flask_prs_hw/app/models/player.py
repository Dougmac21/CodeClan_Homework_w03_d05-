class Player():

    def __init__(self, name, game_choice):
        self.name = name
        self.game_choice = game_choice
        self.valid_choices = ("Paper", "Rock", "Scissors", "Lizard", "Spock")

    def check_player_choice_is_valid(self):
        for choice in self.valid_choices:
            if choice != self.game_choice:
                return "You must choose Paper, Rock, Scissors, Lizard or Spock."

    



    
