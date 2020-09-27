class Prs():

    # def __init__(self, player_1, player_2):
    #     self.player_1 = player_1
    #     self.player_2 = player_2
        

    def play_game(self, player_1, player_2):
        if player_1.game_choice == player_2.game_choice:
            return "It's a tie!"
        else:
            return "Somebody has won!"





        # elif player_1_choice == "Rock" and player_2_choice == "Paper":
        #     return f"{player_2_choice} wraps {player_1_choice}. {self.player_2.name} wins"
        # elif player_1_choice == "Rock" and player_2_choice == "Scissors":
        #     return f"{player_1_choice} smashes {player_2_choice}. {self.player_1.name} wins"
        # elif player_1_choice == "Scissors" and player_2_choice == "Rock":
        #     return f"{player_2_choice} smashes {player_1_choice}. {self.player_2.name} wins"
        # elif player_1_choice == "Scissors" and player_2_choice == "Paper":
        #     return f"{player_1_choice} cuts {player_2_choice}. {self.player_1.name} wins"
        # elif player_1_choice == "Paper" and player_2_choice == "Scissors":
        #     return f"{player_2_choice} cuts {player_1_choice}. {self.player_2.name} wins"
        # elif player_1_choice == "Paper" and player_2_choice == "Rock":
        #     return f"{player_1_choice} wraps {player_2_choice}. {self.player_1.name} wins"