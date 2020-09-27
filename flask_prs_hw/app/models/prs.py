class Prs():

    # def __init__(self, player_1, player_2):
    #     self.player_1 = player_1
    #     self.player_2 = player_2
        

    def play_game(self, player_1, player_2):

        permitted_choices = ("Paper", "Rock", "Scissors")

        if player_1.game_choice not in permitted_choices:
            return "Player 1 must pick Paper, Rock or Scissors!"
        
        if player_2.game_choice not in permitted_choices:
            return "Player 2 must pick Paper, Rock or Scissors!"
        
        if player_1.game_choice == player_2.game_choice:
            return "It's a tie!"

        elif player_1.game_choice == "Paper":
            if player_2.game_choice == "Rock":
                return "Player 1 wins!"
            elif player_2.game_choice == "Scissors":
                return "Player 2 wins!"
        
        elif player_1.game_choice == "Rock":
            if player_2.game_choice == "Scissors":
                return "Player 1 wins!"
            elif player_2.game_choice == "Paper":
                return "Player 2 wins!"
        
        elif player_1.game_choice == "Scissors":
            if player_2.game_choice == "Paper":
                return "Player 1 wins!"
            elif player_2.game_choice == "Rock":
                return "Player 2 wins!"